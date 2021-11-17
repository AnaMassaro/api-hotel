from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from models.models import db
from routes.user_bp import user_bp
from routes.employee_bp import employee_bp

app = Flask(__name__)
CORS(app)

app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(employee_bp, url_prefix='/employee')

if __name__ == '__main__':
  app.run(debug=True)
