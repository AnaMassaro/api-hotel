from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from models.models import db
from routes.user_bp import user_bp
from routes.employee_bp import employee_bp
from routes.bedroom_bp import bedroom_bp
from routes.booking_bp import booking_bp

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

app.config['CORS_HEADERS'] = 'Content-Type'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(employee_bp, url_prefix='/employee')
app.register_blueprint(bedroom_bp, url_prefix='/bedroom')
app.register_blueprint(booking_bp, url_prefix='/booking')

if __name__ == '__main__':
  app.run(debug=True)
