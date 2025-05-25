from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)
    mood_logs = db.relationship('MoodLog', backref='user', lazy=True)

# MoodLog Model
class MoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(50))
    note = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Virtual Companion (OOP Concept)
class VirtualCompanion:
    def respond(self, mood):
        return "How are you feeling today?"

class CheerfulCompanion(VirtualCompanion):
    def respond(self, mood):
        return f"😊 You said you're feeling {mood}. Let's turn that into something better!"

class CalmCompanion(VirtualCompanion):
    def respond(self, mood):
        return f"😌 You're feeling {mood}. Take a deep breath. I'm here with you."
