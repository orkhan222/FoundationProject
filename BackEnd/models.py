from web import app,db

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100),nullable=False)
    soyad = db.Column(db.String(100),nullable=False)
    nomre = db.Column(db.String(100),nullable=False)
    mesaj = db.Column(db.String,nullable=False)
    mail = db.Column(db.String(100),nullable=False)

class HomeBlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(100),nullable=False)
    img = db.Column(db.String(100),nullable=False)


