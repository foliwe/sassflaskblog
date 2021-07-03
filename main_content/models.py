from main_content import db, login_manager
from datetime import datetime


from werkzeug.security import  generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


class User(db.Model,UserMixin):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  profile_image = db.Column(db.String(64), nullable=False, default='default.png')
  email = db.Column(db.String(64),unique=True,index=True)
  username = db.Column(db.String(64),unique=True,index=True)
  password_hash = db.Column(db.String(128))

  posts = db.relationship('Blog', backref='author', lazy=True)

  def __init__(self, username, email, password):
    self.email =email
    self.username =username
    self.password_hash = generate_password_hash(password)


  def check_password_hash(self, password):
    return check_password_hash(self.password_hash, password)


  def __repr__(self):
    return self.username



class Blog(db.Model):
  __tablename__ = 'blogs'

  user = db.relationship(User)
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(64))
  description = db.Column(db.Text,nullable=False)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, title, description, user_id):
    self.title =title
    self.description =description
    self.user_id =  user_id


  def __repr__(self):
    return f'{self.id} {self.user_id}'