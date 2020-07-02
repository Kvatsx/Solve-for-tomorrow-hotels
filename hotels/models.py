from hotels.db import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String, nullable=False)
    emailID = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    wishlist = db.relationship('Wishlist', backref='user', uselist=False)

class Hotel(db.Model):
    __tablename__ = "hotels"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    locid = db.Column(db.String, nullable=False)
    # TODO: create schema of hotels


class Wishlist(db.Model):
    __tablename__ = "wishlist"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    # TODO: design schema of the wishlist
