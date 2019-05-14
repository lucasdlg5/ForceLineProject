# -*- coding: utf-8 -*-
import pymysql
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import session
from flaskext.mysql import MySQL
from flask_cors import CORS


from model import UserModel
from model import TaskModel

app = Flask(__name__, template_folder='template')
mysql = MySQL()
CORS(app)

# mysql configurations
app.config['MYSQL_DATABASE_USER'] = 'basic'
app.config['MYSQL_DATABASE_PASSWORD'] = 'basic123'
app.config['MYSQL_DATABASE_DB'] = 'Todo'
app.config['MYSQL_DATABASE_HOST'] = '134.209.76.136'
mysql.init_app(app)

# FUNCOES DE RENDERIZACAO
def login_render_view():
  return render_template('index.html')

def home_render_view():
  return render_template('home.html')

# VIEWS
@app.route('/', methods=['GET', 'POST'])
def root():
  return login_render_view()

@app.route('/home', methods=['GET', 'POST'])
def home():
  return home_render_view()

# USER ROUTES
@app.route('/user/add', methods=['POST'])
def addUser():
  if UserModel.addUser(request, mysql):
    return jsonify({'email': request.json['email']})
  else:
    return jsonify({'email': ''})

@app.route('/user/findbyname/<string:name>', methods=['GET'])
def findUserByName(name):
  return jsonify(UserModel.findByName(name, mysql))

@app.route('/user/login', methods=['POST'])
def userLogin():
  user = UserModel.valideteLogin(request.json['email'], request.json['password'], mysql)
  if (user != None):
    return jsonify({'email': user[0]['usr_email'], 'id': user[0]['usr_id']})
  else:
    return jsonify({'email': '', 'id': ''})

# TASK ROUTES
@app.route('/task/add', methods=['POST'])
def addTask():
  if (TaskModel.addTask(request, mysql)):
    return jsonify({'success': '1'})
  else:
    return jsonify({'success': '0'})

@app.route('/task/getAll/<int:id>', methods=['GET'])
def getAll(id):
  model = TaskModel.getAllTasks(id, mysql)
  if model != None:
    return jsonify({'len': 0}, model)
  else:
    jsonify({'len': 0})

@app.route('/task/remove/<int:id>')
def removeTask(id):
  if(TaskModel.removeTask(id, mysql)):
    return 'removed'
  else:
    return 'not removed'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)









