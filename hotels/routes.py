from flask import session, render_template, request, redirect, url_for, abort, jsonify
from flask import Flask
from flask_session import Session
from hotels import app
from hotels.models import *
from addict import Dict

from .getHotelsData import get_goibibo_data, getCitiesMapping, getSampleHotels

config_object = 'hotels.settings'
app.config.from_object(config_object)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rupav@localhost/postgres'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
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

        #TODO
        # Check if user already exist with this email id
        # else create a new user

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("LoginInputEmail")
        password = request.form.get("LoginInputPassword")

        # Check for empty fileds
        if email == "" or password == "":
            return redirect(url_for('error', message="Empty fields are not allowed."))
        #TODO: complete login function
    return render_template("login.html")


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        cities = getCitiesMapping()
        params = Dict()
        params.dest = request.form["where"]
        params.cin = request.form["cin"]
        params.cout = request.form["cout"]
        params.guests = request.form["guests"]

        for city in cities:
            if city["name"] == params.dest:
                params.dest = city["id"]
                break

        # fetch data for this region from api in hotels variable, 
        hotels = getSampleHotels()
        print(hotels)

        return render_template('home.html', cities=getCitiesMapping(), show=True, hotels=hotels)
    return render_template('home.html', cities=getCitiesMapping())


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
    data = get_goibibo_data(city_id="8717279093827200968", chk_in="20200703", chk_out="20200704", tvlr="1-2-0", params=params)
    if next != 'null':
        return jsonify({'d': data, 'next': data['next']}), 200
    else:
        return jsonify({'d': data['city_meta_info']['ct'], 'next': data['next']}), 200
        