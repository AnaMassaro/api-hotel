from flask import Blueprint

from controllers.BedroomController import insert, update, list, disable

bedroom_bp = Blueprint('bedroom_bp', __name__)

bedroom_bp.route('/insert', methods=['POST'])(insert)
bedroom_bp.route('/update', methods=['PUT'])(update)
bedroom_bp.route('/list', methods=['GET'])(list)
bedroom_bp.route('/disable', methods=['GET'])(disable)