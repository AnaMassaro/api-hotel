from flask import Blueprint

from controllers.BookingController import insert, list

booking_bp = Blueprint('booking_bp', __name__)

booking_bp.route('/insert', methods=['POST'])(insert)
booking_bp.route('/list', methods=['GET'])(list)