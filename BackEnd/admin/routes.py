from flask_migrate import current
from web import *
from models import *
import os
import random
admin_bp = Blueprint('admin',__name__,url_prefix='/admin',static_folder='static',template_folder='templates')


@admin_bp.route("/contact",methods=['GET','POST'])
def admincontact():
    ctc = Contacts.query.all()
    return render_template('admin/Contact.html',ctc=ctc)


@admin_bp.route("/contact/deletecontact/<int:id>",methods=['GET','POST'])
def admindeletecontact(id):
    db.session.delete(Contacts.query.get(id))
    db.session.commit()
    return redirect('/admin')

@admin_bp.route("/",methods=['GET','POST'])
def homesliders():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"sliders{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Homesliders(title=request.form['title'],text1=request.form['text1'],
            title2=request.form['text2'],span=request.form['span'],image=filePath))
        db.session.commit()
        return redirect('/admin')    
    return render_template('admin/Homesliders.html')


@admin_bp.route("/reklam",methods=['GET','POST'])
def homereklam():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"reklam{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Homereklam(text=request.form['text'],image=filePath))
        db.session.commit()
        return redirect('/admin')    
    return render_template('admin/Homesliders.html')



@admin_bp.route("/bestsellers",methods=['GET','POST'])
def homebestsellers():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"best{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Bestsellers(text=request.form['text'],cost=request.form['cost'],image=filePath))
        db.session.commit()
        return redirect('/admin')    
    return render_template('admin/Homesliders.html')

@admin_bp.route("/mensliders",methods=['GET','POST'])
def mensliders():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"mensliders{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Mensliders(image=filePath))
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
        db.session.add(Menreklam(span=request.form['span'],image=filePath))
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
        db.session.add(Menviawall(text=request.form['text'],cost=request.form['cost'],image=filePath))
        db.session.commit()
        return redirect('/men')    
    return render_template('admin/Men.html')


@admin_bp.route("/womensliders",methods=['GET','POST'])
def womensliders():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"womensliders{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Womensliders(image=filePath))
        db.session.commit()
        return redirect('/women')    
    return render_template('admin/Women.html')

@admin_bp.route("/womenreklam",methods=['GET','POST'])
def womenreklam():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"womenreklam{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Womenreklam(span=request.form['span'],image=filePath))
        db.session.commit()
        return redirect('/women')    
    return render_template('admin/Women.html')


@admin_bp.route("/womenviawall",methods=['GET','POST'])
def womenviawall():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"all{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Womeniawall(text=request.form['text'],cost=request.form['cost'],image=filePath))
        db.session.commit()
        return redirect('/women')    
    return render_template('admin/Women.html')



@admin_bp.route("/about",methods=['GET','POST'])
def about():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"about{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(About(text=request.form['text'],span=request.form['span'],image=filePath))
        db.session.commit()
        return redirect('/about')    
    return render_template('admin/About.html')

    

@admin_bp.route("/productdetail",methods=['GET','POST'])
def productdetail():
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"productdetail{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Productdetail(text=request.form['text'],span=request.form['span'],cost=request.form['cost'],image=filePath))
        db.session.commit()
        return redirect('/productdetail')    
    return render_template('admin/Product.html')