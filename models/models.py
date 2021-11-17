from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String)
  document = db.Column(db.String, unique=True)
  email = db.Column(db.String)
  password = db.Column(db.String(8))
  enabled = db.Column(db.Boolean)

class Employee(db.Model):
  __tablename__ = 'employee'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  document = db.Column(db.String, unique=True)
  email = db.Column(db.String)
  telephone = db.Column(db.String(11))
  role = db.Column(db.String)
  access = db.Column(db.Integer)
  password = db.Column(db.String(8))
  enabled = db.Column(db.Boolean)