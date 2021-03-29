from web import app,db
from models import *
from flask import Flask,render_template,redirect,request,url_for,flash,current_app

@app.route('/',methods=['GET','POST'])
def index():
    homesliders = Homesliders.query.all()
    homereklam = Homereklam.query.all()
    homebestsellers = Bestsellers.query.all()
    return render_template("web/index.html",sliders=homesliders,reklam=homereklam,best=homebestsellers)

@app.route('/about',methods=['GET','POST'])
def about():
    about = About.query.all()
    return render_template("web/about.html",about=about)

@app.route('/addshoes',methods=['GET','POST'])
def addshoes():
    return render_template("web/addshoes.html")

@app.route('/cart',methods=['GET','POST'])
def cart():
    return render_template("web/cart.html")


@app.route('/men',methods=['GET','POST'])
def men():
    mensliders = Mensliders.query.all()
    menreklam = Menreklam.query.all()
    all = Menviawall.query.all()
    return render_template("web/men.html",mensliders=mensliders,menreklam=menreklam,all=all)


@app.route('/women',methods=['GET','POST'])
def women():
    womensliders = Womensliders.query.all()
    womenreklam = Womenreklam.query.all()
    all = Womeniawall.query.all()
    return render_template("web/women.html",womensliders=womensliders,womenreklam=womenreklam,all=all)

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
    productdetail = Productdetail.query.all()
    return render_template("web/product-detail.html",productdetail=productdetail)

