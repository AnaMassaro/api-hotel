from models.User import User
from flask_sqlalchemy import SQLAlchemy
from flask import request

from models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def list():
    return {"user": "ana"}

def insert():
  user = request.json
  print(user['user'])
  
  return {"message": "success"}