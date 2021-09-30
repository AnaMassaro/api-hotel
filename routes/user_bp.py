from flask import Blueprint

from controllers.UserController import list, insert

user_bp = Blueprint('user_db', __name__)

user_bp.route('/list', methods=['GET'])(list)
user_bp.route('/insert', methods=['POST'])(insert)