from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

from models.models import Bedroom

db = SQLAlchemy()

def insert():
  body = request.json

  try:
    bedroom = Bedroom(
      name=body['name'],
      description=body['description'],
      value=body['value'],
      quality=body['quality'],
      status=True,
      enabled=True
    )

    db.session.add(bedroom)
    db.session.commit()

  except Exception as e:
    return {"message": "Failed to insert"}, 400

  return {"message": "success"}, 200

'''
def disable():
  id = request.args.get('id')

  if not id:
    return {"message": "Invalid parameters"}, 400

  try:
    bedroom = Bedroom.query.filter_by(id=id).first()

    bedroom.enabled = False

    db.session.merge(bedroom)
    db.session.commit()

    msg = "success"
    status = 200
  except Exception as e:
    msg = "Failed to disable"
    status = 400

  return {"message": msg}, status
'''

def update():
  id = request.args.get('id')

  if not id:
    return {"message": "Invalid parameters"}, 400

  body = request.json
  try:
    bedroom = Bedroom.query.filter_by(id=id).first()

    if 'name' in body:
      bedroom.bedroom = body['name']
    if 'description' in body:
      bedroom.description = body['description']
    if 'value' in body:
      bedroom.value = body['value']
    if 'quality' in body:
      bedroom.quality = body['quality']

    db.session.merge(bedroom)
    db.session.commit()

    rjson = {
      "id": bedroom.id,
      "name": bedroom.name,
      "description": bedroom.description,
      "value": bedroom.value,
      "quality": bedroom.quality
    }

    return jsonify(rjson), 200

  except Exception as e:
    return {"message": "Failed to update"}, 400

def list():
  rjson = []

  filters = {
    'id': request.args.get('id'),
    'quality': request.args.get('quality'),
    'name': request.args.get('name'),
    'value': request.args.get('value'),
  }

  if not filters:
    bedrooms = Bedroom.query.filter_by(enabled=True).all()

    for bedroom in bedrooms:
      rjson.append({
        "id": bedroom.id,
        "name": bedroom.name,
        "description": bedroom.description,
        "quality": bedroom.quality,
        "value": bedroom.value,
      })

  elif filters['id']:
    bedroom = Bedroom.query.filter_by(id=int(filters['id'])).first()
    rjson.append({
      "id": bedroom.id,
      "name": bedroom.name,
      "description": bedroom.description,
      "quality": bedroom.quality,
      "value": bedroom.value,
    })
  else:
    sql = """
      SELECT * FROM bedrooms WHERE enabled = true
    """
    bind = []

    if filters['quality']:
      sql += " AND quality = "+filters['quality']+" "
    if filters['value']:
      sql += " AND value <= "+filters['value']+" "

    bedrooms = db.engine.execute(sql)

    for bedroom in bedrooms:
      rjson.append({
        "id": bedroom.id,
        "name": bedroom.name,
        "description": bedroom.description,
        "quality": bedroom.quality,
        "value": bedroom.value,
      })

  return jsonify(rjson), 200