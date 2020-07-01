from flask import session, render_template, request, redirect, url_for, abort, jsonify
from flask import Flask
from flask_session import Session
from hotels import app
from hotels.models import *

db.init_app(app)

from .getHotelsData import get_goibibo_data


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


@app.route('/testapi/next=<next>', methods=['GET'])
def api(next):
    params = (
        ('s', 'popularity^'),
        ('cur', 'INR^'),
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
        