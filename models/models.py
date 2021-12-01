from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String)
  document = db.Column(db.String, unique=True)
  email = db.Column(db.String)
  password = db.Column(db.String(100))
  enabled = db.Column(db.Boolean)

class Employee(db.Model):
  __tablename__ = 'employees'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  document = db.Column(db.String, unique=True)
  email = db.Column(db.String)
  telephone = db.Column(db.String(11))
  role = db.Column(db.String)
  access = db.Column(db.Integer)
  password = db.Column(db.String(100))
  enabled = db.Column(db.Boolean)

class Bedroom(db.Model):
  __tablename__ = 'bedrooms'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  description = db.Column(db.String)
  value = db.Column(db.Float)
  quality = db.Column(db.Integer)

class Booking(db.Model):
  __tablename__ = 'bookings'

  id = db.Column(db.Integer, primary_key=True)
  id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
  id_bedroom = db.Column(db.Integer, db.ForeignKey('bedrooms.id'))
  start_date = db.Column(db.Date)
  end_date = db.Column(db.Date)
  status = db.Column(db.String)
