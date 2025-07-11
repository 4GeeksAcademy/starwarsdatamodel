from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    subscription_date = db.Column(db.DateTime, default=datetime.utcnow)

    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(50))
    birth_year = db.Column(db.String(20))
    eye_color = db.Column(db.String(50))

    favorites = db.relationship('Favorite', backref='character', lazy=True)

    def __repr__(self):
        return f'<Character {self.name}>'


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(100))
    population = db.Column(db.String(100))
    terrain = db.Column(db.String(100))

    favorites = db.relationship('Favorite', backref='planet', lazy=True)

    def __repr__(self):
        return f'<Planet {self.name}>'


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(
        db.Integer, db.ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(
        db.Integer, db.ForeignKey('planet.id'), nullable=True)

    def __repr__(self):
        return f'<Favorite User:{self.user_id}, Char:{self.character_id}, Planet:{self.planet_id}>'

