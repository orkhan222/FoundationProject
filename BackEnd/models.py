from web import app,db

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100),nullable=False)
    soyad = db.Column(db.String(100),nullable=False)
    nomre = db.Column(db.String(100),nullable=False)
    mesaj = db.Column(db.String,nullable=False)
    mail = db.Column(db.String(100),nullable=False)

class Homesliders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    text1 = db.Column(db.String,nullable=False)
    title2 = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class Homereklam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)


class Bestsellers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class Mensliders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)

class Menreklam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)

class Menviawall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class Womensliders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)

class Womenreklam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)

class Womeniawall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)

class Productdetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)