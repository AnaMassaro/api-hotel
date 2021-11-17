from flask import Blueprint

from controllers.EmployeeController import insert, update, disable, list, login

employee_bp = Blueprint('employee_bp', __name__)

employee_bp.route('/insert', methods=['POST'])(insert)
employee_bp.route('/update', methods=['PUT'])(update)
employee_bp.route('/disable', methods=['GET'])(disable)
employee_bp.route('/list', methods=['GET'])(list)
employee_bp.route('/login', methods=['POST'])(login)