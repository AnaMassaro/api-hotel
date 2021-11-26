from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from models.models import Booking

db = SQLAlchemy()

def booking_details(id):
  sql = """
    select 
      bookings.id as id_booking,
      bedrooms.name,
      bedrooms.id as number_bedroom,
      bookings.start_date,	
      users.user
    from bookings inner join bedrooms 
      on bookings.id_bedroom = bedrooms.id 
      inner join users on bookings.id_user = users.id
      where 1 = 1
    """
  try:
    sql += " AND bookings.id = "+str(id)+" "
    booking = db.engine.execute(sql)

    for row in booking:
      rjson = {
        "id_booking": row[0],
        "room_name": row[1],
        "room_number": row[2],
        "start_date": row[3],
        "user_name": row[4]
      }

  except Exception as e:
    db.session.rollback()
    return ""

  return rjson

def insert():
  body = request.json

  try:
    booking = Booking(
      id_user=body['id_user'], 
      id_bedroom=body['id_bedroom'],
      start_date=body['start_date'],
      end_date=body['end_date'],
      status='PENDENTE'
    )

    db.session.add(booking)
    db.session.commit()

    sql = """
      SELECT * FROM bookings WHERE id IN (SELECT MAX(id) FROM bookings)
    """

    last_booking = db.engine.execute(sql)

    for row in last_booking:
      id = row[0]

    result = booking_details(id)
  except Exception as e:
    db.session.rollback()
    return {"message": "Failed to insert"}, 400
  
  return jsonify(result), 200

