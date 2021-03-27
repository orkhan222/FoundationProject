from flask import Flask,render_template,redirect,request,url_for,flash,current_app,Blueprint
from flask_migrate import Migrate,MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager



app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/database.db'
app.config['UPLOAD_PATH'] ='admin/static/upload'

db = SQLAlchemy(app) 
migrate = Migrate(app, db, render_as_batch=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *
from web.routes import *
import admin
