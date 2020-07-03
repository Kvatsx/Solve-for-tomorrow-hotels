from flask import Flask, session, render_template, request, redirect, url_for, abort, jsonify, flash
from flask_session import Session
from hotels import app
# from hotels.models import *
from addict import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .getHotelsData import get_goibibo_data, getCitiesMapping, getSampleHotels

config_object = 'hotels.settings'
app.config.from_object(config_object)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine("postgres://cuhpqttlfncjia:ab42abc2241221dcd463d198a2c561fe0d1398137ac9945c1c749c5a932a088d@ec2-52-204-232-46.compute-1.amazonaws.com:5432/d2qn5k3635hjih")
db = scoped_session(sessionmaker(bind=engine))

# with app.app_context():
#     db.create_all()

@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("RegisterFullName")
        email = request.form.get("RegisterInputEmail")
        password = request.form.get("RegisterInputPassword")

        # Check for empty fileds
        if name == "" or email == "" or password == "":
            return redirect(url_for('error', message="Empty fields are not allowed."))

        # Check if user already exist with this email id
        user_id = db.execute("SELECT id FROM Users WHERE email = :email",{"email": email}).fetchone()
        if user_id != None:
            return redirect(url_for('error', message="User already exist with this email id."))

        # else create a new user
        else:
            db.execute("INSERT INTO Users (name, email, password) VALUES (:name, :email, :password)",{
                "name": name, 
                "email": email, 
                "password": password})
            db.commit()
            return redirect(url_for("success"), code=302)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("LoginInputEmail")
        password = request.form.get("LoginInputPassword")

        # Check for empty fileds
        if email == "" or password == "":
            return redirect(url_for('error', message="Empty fields are not allowed."))

        user = db.execute("SELECT id, name FROM Users WHERE email = :email AND password = :password",{"email": email, "password": password}).fetchone()
        if user != None:
            user = list(user)
            print(user)
            session['user'] = user
            print(session)
            return redirect(url_for("home"))
        else:
            return redirect(url_for('error', message="Wrong Credentials."))
    return render_template("login.html")


@app.route("/error")
def error():
    return render_template("error.html", message=request.args.get('message'))


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/logout")
def logout():
    print("Logged in:", session)
    if 'user' not in session:
        print("Login now!")
        return redirect(url_for("login"))
    print("[INFO] Logout called!")
    print(session)
    session.pop("user", None)
    print(session)
    return redirect(url_for('index'))

# @app.route('/home', methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         if "add" in request.form:
#             ''' get input from forms all those hotels which are added by user to wishlist
#             '''
#             hotels = []
#             for hotel in hotels:
#                 db.session.add(Hotel(hotel))
#                 db.session.commit()
#             db.session.close()
            
#             flash("Added to your wishlist!", "success")
#             return render_template('home.html', cities=getCitiesMapping())
#         else:
#             flash("Lets find you a stay!")
#             cities = getCitiesMapping()
#             params = Dict()
#             params.dest = request.form["where"]
#             params.cin = request.form["cin"]
#             params.cout = request.form["cout"]
#             params.guests = request.form["guests"]

#             for city in cities:
#                 if city["name"] == params.dest:
#                     params.dest = city["id"]
#                     break

#             # fetch data for this region from api in hotels variable, 
#             hotels = get_goibibo_data(city_id=params.dest)
#             return jsonify(hotels)
#             return render_template('home.html', cities=getCitiesMapping(), show=True, hotels=hotels)
#     flash("Hi There!")
#     return render_template('home.html', cities=getCitiesMapping(), user_name=session.get('user')[1])


@app.route('/home')
def home():
    print("Logged in:", session)
    if 'user' not in session:
        print("Login now!")
        return redirect(url_for("login"))
    return render_template('home.html', cities=getCitiesMapping(), user_name=session.get('user')[1])


@app.route("/getHotels", methods=["POST"])
def getHotels():
    if request.method == "POST":
        city_id = str(request.form.get('city_id'))
        checkin = str(request.form.get('checkin'))
        checkout = str(request.form.get('checkout'))
        guestroom = str(request.form.get('guestrooms'))
        nextpage = str(request.form.get('next'))

        checkin = checkin.replace("-", "")
        checkout = checkout.replace("-", "")

        params = (
            ('s', 'popularity'),
            ('cur', 'INR'),
            ('tmz', '-330'),
        )
        if nextpage != "null":
            params = (('next', nextpage), ) + params
        data, status = get_goibibo_data(city_id=city_id, chk_in=checkin, chk_out=checkout, tvlr=guestroom, params=params)
        if status == 200:
            return jsonify({"data": data, "success":True}), 200
        else:
            return jsonify({"success": False}), 404
    return jsonify({"error": 404}), 404


@app.route("/mywishlist", methods=["GET"])
def wishlist():
    return render_template('wishlist.html')

@app.route('/testapi/next=<next>', methods=['GET'])
def api(next):
    params = (
        ('s', 'popularity'),
        ('cur', 'INR'),
        ('tmz', '-330'),
    )
    if next != "null":
        params = (('next', next), ) + params
    print(params)
    data, status = get_goibibo_data(city_id="8717279093827200968", chk_in="20200703", chk_out="20200704", tvlr="1-2-0", params=params)
    if status == 200:
        return jsonify(data), 200
    else:
        return jsonify(data), 404


@app.route('/addToWishlist')
def addtowishlist():
    if request.method == "POST":
        print("ok")
    return render_template('wishlist.html', user_name=session.get('user')[1])

# {
#         "hotel_name": "Riva Beach Resort",
#         "location": "Pernem",
#         "image": "https://cdn1.goibibo.com/t_g_ing_v8/riva-beach-resort-goa-exterior-142052201679-orig.webp",
#         "score": 4.3,
#         "reviewCount": 881,
#         "ratingCount": 1426,
#         "offeringPrice": 2340,
#         "specialPrice": 1496,
#         "tnc": 340
# }        