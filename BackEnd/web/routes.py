from web import app,db
from flask import Flask,render_template,redirect,request,url_for,flash,current_app


@app.route('/',methods=['GET','POST'])
def index():
    return render_template("web/index.html")


@app.route('/about',methods=['GET','POST'])
def about():
    return render_template("web/about.html")

@app.route('/addshut',methods=['GET','POST'])
def addshut():
    return render_template("web/addshut.html")



    