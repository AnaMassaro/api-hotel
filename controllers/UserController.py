from models.User import User
from flask_sqlalchemy import SQLAlchemy
from flask import request

from models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def list():
    return {"user": "ana"}

def insert():
  body = request.json

  user = User(
    user=body['user'], 
    document=body['document'],
    email=body['email'],
    password=body['password'],
    enabled=True
  )

  db.session.add(user)
  db.session.commit()
  
  return {"message": "success"}