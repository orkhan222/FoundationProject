from web import app,db
from models import *
from flask import Flask,render_template,redirect,request,url_for,flash,current_app

@app.route('/',methods=['GET','POST'])
def index():
    
    return render_template("web/index.html")

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template("web/about.html")

@app.route('/addshoes',methods=['GET','POST'])
def addshoes():
    return render_template("web/addshoes.html")

@app.route('/cart',methods=['GET','POST'])
def cart():
    return render_template("web/cart.html")


@app.route('/men',methods=['GET','POST'])
def men():
    return render_template("web/men.html")


@app.route('/women',methods=['GET','POST'])
def women():
    return render_template("web/women.html")

@app.route('/order',methods=['GET','POST'])
def order():
    return render_template("web/order-complete.html")

@app.route('/checkout',methods=['GET','POST'])
def checkout():
    return render_template("web/checkout.html")


@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        ctc = Contacts(ad=request.form['ad'],soyad=request.form['soyad'],
            nomre=request.form['nomre'],mail=request.form['mail'],mesaj=request.form['mesaj'])
        db.session.add(ctc)
        db.session.commit()
        return redirect ('/contact')
    return render_template("web/contact.html")


@app.route('/product',methods=['GET','POST'])
def product():
    return render_template("web/product-detail.html")

