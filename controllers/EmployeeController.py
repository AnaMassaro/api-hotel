from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from models.models import Employee

db = SQLAlchemy()

def insert():
  body = request.json

  try:
    employee = Employee(
      name=body['name'], 
      document=body['document'],
      email=body['email'],
      telephone=body['telephone'],
      role=body['role'],
      access=body['access'],
      password=generate_password_hash(body['password'], method='sha256'),
      enabled=True
    )

    db.session.add(employee)
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
    employee = Employee.query.filter_by(id=id).first()

    if 'name' in body:
      employee.name = body['name']
    if 'email' in body:
      employee.email = body['email']
    if 'password' in body:
      employee.password = generate_password_hash(body['password'], method='sha256')
    if 'telephone' in body:
      employee.telephone = body['telephone']
    if 'role' in body:
      employee.role = body['role']
    if 'access' in body:
      employee.access = body['access']

    db.session.merge(employee)
    db.session.commit()

    rjson = {
      "id": employee.id,
      "name": employee.name,
      "document": employee.document,
      "email": employee.email,
      "role": employee.role,
      "telephone": employee.telephone,
      "access": employee.access,
    }

    return jsonify(rjson), 200
  except Exception as e:
    return {"message": "Failed to update"}, 400

def disable():
  id = request.args.get('id')

  if not id:
    return {"message": "Invalid parameters"}, 400

  try:
    employee = Employee.query.filter_by(id=id).first()

    employee.enabled = False

    db.session.merge(employee)
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

  try:
    if not id:
      employees = Employee.query.filter_by(enabled=True).all()

      for employee in employees:
        rjson.append({
          "id": employee.id,
          "name": employee.name,
          "document": employee.document,
          "email": employee.email,
          "telephone": employee.telephone,
          "role": employee.role,
          "access": employee.access,
        })
    else:
      employee = Employee.query.filter_by(id=id).first()
      rjson.append({
          "id": employee.id,
          "name": employee.name,
          "document": employee.document,
          "email": employee.email,
          "telephone": employee.telephone,
          "role": employee.role,
          "access": employee.access,
      })

    return jsonify(rjson), 200
  except Exception as e:
    return {"message": "Failed to list"}, 400

def login():
  body = request.json

  email = body['email']
  password = body['password']

  employee = Employee.query.filter_by(email=email).first()

  if not employee or not check_password_hash(employee.password, password):
    return {"message": "Failed to login"}, 400

  rjson = {
    "id": employee.id,
    "name": employee.name,
    "document": employee.document,
    "email": employee.email,
    "role": employee.role,
    "telephone": employee.telephone,
    "access": employee.access,
  }

  return jsonify(rjson), 200