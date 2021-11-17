from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

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
      password=body['password'],
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

    employee.name = body['name']
    employee.email = body['email']
    employee.telephone = body['telephone']
    employee.role = body['role']
    employee.access = body['access']
    employee.password = body['password']

    db.session.merge(employee)
    db.session.commit()

    msg = "success"
    status = 200
  except Exception as e:
    msg = "Failed to update"
    status = 400

  return {"message": msg}, status

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
          "password": employee.password,
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
          "password": employee.password,
      })

    return jsonify(rjson), 200
  except Exception as e:
    return {"message": "Failed to list"}, 400