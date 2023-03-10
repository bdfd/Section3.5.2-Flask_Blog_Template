'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-12-10 12:06:45
LastEditors  : BDFD
Description  : 
FilePath     : \app.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from admin.admin import admin
# from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import users
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)
app.register_blueprint(admin, url_prefix="/admin")

# db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

# class users(db.Model):
#   _id = db.Column('id', db.Integer, primary_key=True)
#   name = db.Column('name', db.String(100))
#   email = db.Column('email', db.String(100))

#   def __init__(self, name, email):
#     self.name = name
#     self.email = email

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/view')
def view():
  all_user = users.query.all()
  return render_template('view.html', values=all_user)

@app.route('/login', methods=['POST','GET'])
def login():
  if request.method == 'POST':
    session.permanent = True
    user = request.form['nm']
    session['user'] = user
    found_user = users.query.filter_by(name=user).first()
    if found_user:
      session['email'] = found_user.email

    else:
      usr = users(user, '')
      db.session.add(usr)
      db.session.commit()
    flash('Login Successful!')
    return redirect(url_for('user'))
  else:
    if 'user' in session:
      flash('Already Logged In!')
      return redirect(url_for('user'))
    return render_template('login.html')

@app.route('/user', methods=['POST','GET'])
def user():
  email = None
  if 'user' in session:
    user = session['user']
    if request.method == 'POST':
      email = request.form['email']
      session['email'] = email
      found_user = users.query.filter_by(name=user).first()
      found_user.email = email
      db.session.commit()
      flash('Email was saved!')
    else:
      if 'email' in session:
        email = session['email']
    return render_template('user.html', user=user, email=email)
  else:
    flash('You are not logged in!')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  if 'user' in session:
    user = session['user']  
    flash(f'You have been logged out, {user}.','info')
  session.pop('user', None)
  session.pop('email', None)
  return redirect(url_for('login'))

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
