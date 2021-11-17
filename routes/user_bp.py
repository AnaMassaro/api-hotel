from flask import Blueprint

from controllers.UserController import insert, update, disable, list

user_bp = Blueprint('user_db', __name__)

user_bp.route('/insert', methods=['POST'])(insert)
user_bp.route('/update', methods=['PUT'])(update)
user_bp.route('/disable', methods=['GET'])(disable)
user_bp.route('/list', methods=['GET'])(list)