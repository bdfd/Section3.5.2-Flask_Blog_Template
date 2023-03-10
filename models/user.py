'''
Date         : 2022-12-09 18:12:42
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-12-10 11:33:49
LastEditors  : BDFD
Description  : 
FilePath     : \model.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''

from extensions import db

class users(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True)
  name = db.Column('name', db.String(100))
  email = db.Column('email', db.String(100))

  def __init__(self, name, email):
    self.name = name
    self.email = email