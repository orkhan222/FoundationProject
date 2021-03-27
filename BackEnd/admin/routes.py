from flask_migrate import current
from web import *
from models import *
admin_bp = Blueprint('admin',__name__,url_prefix='/admin',static_folder='static',template_folder='templates')


@admin_bp.route("/",methods=['GET','POST'])
def adminindex():
    ctc = Contacts.query.all()
    return render_template('admin/index.html',ctc=ctc)


@admin_bp.route("/deletecontact/<int:id>",methods=['GET','POST'])
def admindeletecontact(id):
    db.session.delete(Contacts.query.get(id))
    db.session.commit()
    return redirect('/admin')

@admin_bp.route('/blog',methods=['GET','POST'])
def adminBlog():
    if not current_user.is_authenticated:
        return redirect('/auth')
    blog=Blogs.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"blog{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Blogs(basliq=request.form['basliq'],img=filePath))
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/Home_blog.html',blog=blog)

@admin_bp.route('/deleteform/<int:id>')
def adminDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    db.session.delete(Form.query.get(id))
    db.session.commit()
    return redirect('/admin')

@admin_bp.route('/deleteblog/<int:id>')
def blogDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    blog=Blogs.query.get(id)
    os.unlink(os.getcwd() + blog.blogImage)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/admin/blog')



