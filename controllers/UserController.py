from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from models.models import User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

def insert():
  body = request.json

  try:
    user = User(
      user=body['name'], 
      document=body['document'],
      email=body['email'],
      password=generate_password_hash(body['password'], method='sha256'),
      enabled=True
    )

    db.session.add(user)
    db.session.commit()

  except IntegrityError:
    db.session.rollback()
    return {"message": "This member already exists"}, 400
  
  return {"message": "success"}, 200

def update():
  id = request.args.get('id')
  
  if not id:
    return {"message": "Invalid parameters"}, 400

  body = request.json
  try:
    user = User.query.filter_by(id=id).first()

    if 'name' in body:
      user.user = body['name']
    if 'email' in body:
      user.email = body['email']
    if 'password' in body:
      user.password = generate_password_hash(body['password'], method='sha256')

    db.session.merge(user)
    db.session.commit()

    rjson = {
      "id": user.id,
      "name": user.user,
      "document": user.document,
      "email": user.email,
    }

    return jsonify(rjson), 200
  except Exception as e:
    return {"message": "Failed to update"}, 400

def disable():
  id = request.args.get('id')

  if not id:
    return {"message": "Invalid parameters"}, 400

  try:
    user = User.query.filter_by(id=id).first()

    user.enabled = False

    db.session.merge(user)
    db.session.commit()

    msg = "success"
    status = 200
  except Exception as e:
    msg = "Failed to disable"
    status = 400

  return {"message": msg}, status

def list():
  id = request.args.get('id')
  rjson = []

  if not id:
    users = User.query.filter_by(enabled=True).all()

    for user in users:
      rjson.append({
        "id": user.id,
        "name": user.user,
        "document": user.document,
        "email": user.email,
      })
  else:
    users = User.query.filter_by(id=id).first()
    rjson.append({
      "id": users.id,
      "name": users.user,
      "document": users.document,
      "email": users.email,
    })

  return jsonify(rjson), 200

def login():
  body = request.json

  email = body['email']
  password = body['password']

  user = User.query.filter_by(email=email).first()

  if not user or not check_password_hash(user.password, password):
    return {"message": "Failed to login"}, 400

  rjson = {
    "id": user.id,
    "name": user.user,
    "document": user.document,
    "email": user.email,
  }

  return jsonify(rjson), 200

  