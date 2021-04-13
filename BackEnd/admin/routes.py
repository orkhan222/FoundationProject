from flask_migrate import current
from web import *
from models import *
import os
import random
admin_bp = Blueprint('admin',__name__,url_prefix='/admin',static_folder='static',template_folder='templates')

# /////////////////////  CONTACT//////////////////////////////////////////
@admin_bp.route("/contact",methods=['GET','POST'])
def admincontact():
    ctc = Contacts.query.all()
    return render_template('admin/Contact.html',ctc=ctc)


@admin_bp.route("/contact/deletecontact/<int:id>",methods=['GET','POST'])
def admindeletecontact(id):
    db.session.delete(Contacts.query.get(id))
    db.session.commit()
    return redirect('/admin')
# /////////////////////////// CONTACT BITDI/////////////////////////////////////
@admin_bp.route("/",methods=['GET','POST'])
def homesliders():
    slide = Homesliders.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"sliders{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Homesliders(
            title=request.form['title'],
            text1=request.form['text1'],
            title2=request.form['text2'],
            span=request.form['span'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/admin')    
    return render_template('admin/Homesliders.html',slide=slide)


@admin_bp.route("/deleteslide/<int:id>",methods=['GET','POST'])
def deleteslide(id):
    B=Homesliders.query.get(id)
    db.session.delete(B)
    db.session.commit()
    return redirect('/admin')


@admin_bp.route("/reklam",methods=['GET','POST'])
def homereklam():
    rekllam = Homereklam.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"reklam{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Homereklam(
            text=request.form['text'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/admin')    
    return render_template('admin/Homesliders.html',rekllam=rekllam)

@admin_bp.route("/deletereklam/<int:id>",methods=['GET','POST'])
def deletereklam(id):
    C=Homereklam.query.get(id)
    db.session.delete(C)
    db.session.commit()
    return redirect('/admin')

@admin_bp.route("/bestsellers",methods=['GET','POST'])
def homebestsellers():
    seller = Bestsellers.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"best{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Bestsellers(
            text=request.form['text'],
            cost=request.form['cost'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/admin')    
    return render_template('admin/Homesliders.html',seller=seller)


@admin_bp.route("/deletesellers/<int:id>",methods=['GET','POST'])
def deletesellers(id):
    A=Bestsellers.query.get(id)
    db.session.delete(A)
    db.session.commit()
    return redirect('/admin')

# /////////////////////////////HOME HISSE BITDI ////////////////////////////////////////////////////////




@admin_bp.route("/mensliders",methods=['GET','POST'])
def mensliders():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"mensliders{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Mensliders(
            image=filePath)
        )
        db.session.commit()
        return redirect('/men')    
    return render_template('admin/Men.html')




@admin_bp.route("/menreklam",methods=['GET','POST'])
def menreklam():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"menreklam{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Menreklam(
            span=request.form['span'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/men')    
    return render_template('admin/Men.html')


@admin_bp.route("/menviawall",methods=['GET','POST'])
def menviawall():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"all{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Menviawall(
            text=request.form['text'],
            cost=request.form['cost'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/men')    
    return render_template('admin/Men.html')

# ////////////////////////////////////// Men hisse bitdi////////////////////////////////////////////////
@admin_bp.route("/womenSlide",methods=['GET','POST'])
def womenSlide():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"womenslider{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(WomenSlide(
            image=filePath)
        )
        db.session.commit()
        return redirect('/women')    
    return render_template('admin/Women.html')

@admin_bp.route("/womenReklam",methods=['GET','POST'])
def womenReklam():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"womenReklam{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(WomenReklam(
            span=request.form['span'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/women')    
    return render_template('admin/Women.html')


@admin_bp.route("/WomenAll",methods=['GET','POST'])
def womenAll():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"womenAll{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(WomenAll(
            text=request.form['text'],
            cost=request.form['cost'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/women')    
    return render_template('admin/Women.html')

# ////////////////////////////////////Women hisse bitdi ////////////////////////////////////////////

@admin_bp.route("/about",methods=['GET','POST'])
def about():
    about=About.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"about{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(About(
            text=request.form['text'],
            span=request.form['span'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/about')    
    return render_template('admin/About.html',about=about)

    # ///////////////////////////ABOUT HISSE BITDI///////////////////////////////////////






@admin_bp.route("/checkout",methods=['GET','POST'])
def admincheckout():
    chec = Checkout.query.all()
    return render_template('admin/Checkout.html',chec=chec)

@admin_bp.route("/checkout/deletecheckout/<int:id>",methods=['GET','POST'])
def admindeletecheckout(id):
    db.session.delete(Checkout.query.get(id))
    db.session.commit()
    return redirect('/admin')

# ///////////////////////////////////  Checkout BITDI  //////////////////////////////

    
@admin_bp.route("/cart",methods=['GET','POST'])
def cart():
    cart = Cart.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"cart{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Cart(
            text=request.form['text'],
            total=request.form['total'],
            quantity=request.form['quantity'],
            price=request.form['price'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/cart')    
    return render_template('admin/Cart.html',cart=cart)


@admin_bp.route("/cart/deletecart/<int:id>",methods=['GET','POST'])
def deletecart(id):
    db.session.delete(Cart.query.get(id))
    db.session.commit()
    return redirect('/admin')



@admin_bp.route("/related",methods=['GET','POST'])
def cartrelated():
    related = Related.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"related{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Related(
            text=request.form['text'],
            cost=request.form['cost'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/related')    
    return render_template('admin/Cart.html',related=related)

@admin_bp.route("/cart/deleterelated/<int:id>",methods=['GET','POST'])
def deletecartrelated(id):
    db.session.delete(Related.query.get(id))
    db.session.commit()
    return redirect('/admin')
        
#  ////////////////////////////////////// CART HISSE BITDI///////////////////////////////////////////////////

@admin_bp.route("/wishlist",methods=['GET','POST'])
def wishlist():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"wishlist{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Wishlist(
            text=request.form['text'],
            total=request.form['total'],
            quantity=request.form['quantity'],
            price=request.form['price'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/wishlist')    
    return render_template('admin/Wishlist.html')



@admin_bp.route("/wishlistrelated",methods=['GET','POST'])
def wishlistrelated():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"wishlistrelated{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Wishlistrelated(
            text=request.form['text'],
            cost=request.form['cost'],
            image=filePath)
        )
        db.session.commit()
        return redirect('/wishlistrelated')    
    return render_template('admin/Wishlist.html')
# ///////////////////////////////////////// Wishlist BITDI ////////////////////////////////////////////////////