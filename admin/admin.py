'''
Date         : 2022-12-09 12:54:06
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-12-09 13:09:43
LastEditors  : BDFD
Description  : 
FilePath     : \admin.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')

@admin.route('/home')
@admin.route('/')
def home():
    return render_template('home.html')