from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String)
  password = db.Column(db.String(8))

  @property
  def serialize(self):
    return {
      'id': self.id,
      'user': self.user,
      'password': self.password
    }