from web import app,db
from models import *
from flask import Flask,render_template,redirect,request,url_for,flash,current_app

@app.route('/',methods=['GET','POST'])
def index():
    homesliders = Homesliders.query.all()
    homereklam = Homereklam.query.all()
    homebestsellers = Bestsellers.query.all()
    
    return render_template("web/index.html",sliders=homesliders,reklam=homereklam,best=homebestsellers,cart=cart)

@app.route('/about',methods=['GET','POST'])
def about():
    about = About.query.all()
    return render_template("web/about.html",about=about)

@app.route('/addshoes',methods=['GET','POST'])
def addshoes():
    wishlist = Wishlist.query.all()
    wishlistrelated = Wishlistrelated.query.all()
    return render_template("web/addshoes.html",wishlist=wishlist,wishlistrelated=wishlistrelated)

@app.route('/cart',methods=['GET','POST'])
def cart():
    cart = Cart.query.all()
    cartrelated = Related.query.all()
    related= Related.query.all()
    return render_template("web/cart.html",cart=cart,cartrelated=cartrelated,related=related)


@app.route('/men',methods=['GET','POST'])
def men():
    mensliders = Mensliders.query.all()
    menreklam = Menreklam.query.all()
    all = Menviawall.query.all()
    return render_template("web/men.html",mensliders=mensliders,menreklam=menreklam,all=all)


@app.route('/women',methods=['GET','POST'])
def women():
    womenSlide = WomenSlide.query.all()
    womenReklam = WomenReklam.query.all()
    womenAll = WomenAll.query.all()
    return render_template("web/women.html",womenSlide=womenSlide,womenReklam=womenReklam,womenAll=womenAll)

@app.route('/order',methods=['GET','POST'])
def order():
   
    return render_template("web/order-complete.html")

@app.route('/checkout',methods=['GET','POST'])
def checkout():
    if request.method == 'POST':
        chec = Checkout(
            ad=request.form['ad'],
            soyad=request.form['soyad'],
            nomre=request.form['nomre'],
            email=request.form['email'],
            country=request.form['country'],
            magazadi=request.form['magazadi'],
            adress=request.form['adress'],
            seher=request.form['seher'],
            zip=request.form['zip']
        )
        db.session.add(chec)
        db.session.commit()
        return redirect ('/checkout')
    return render_template("web/checkout.html")


@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        ctc = Contacts(
            ad=request.form['ad'],
            soyad=request.form['soyad'],
            nomre=request.form['nomre'],
            mail=request.form['mail'],
            mesaj=request.form['mesaj']
        )
        db.session.add(ctc)
        db.session.commit()
        return redirect ('/contact')
    return render_template("web/contact.html")


@app.route('/product/<int:id>',methods=['GET','POST'])
def product1(id):
    productdetail = Bestsellers.query.filter_by(id=id)
    return render_template("web/product-detail.html",productdetail=productdetail)

