from flask import Blueprint

from controllers.BookingController import insert

booking_bp = Blueprint('booking_bp', __name__)

booking_bp.route('/insert', methods=['POST'])(insert)