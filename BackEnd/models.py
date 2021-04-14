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

class WomenSlide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)

class WomenReklam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)

class WomenAll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)




class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100),nullable=False)
    country=db.Column(db.String(100),nullable=False)
    soyad = db.Column(db.String(100),nullable=False)
    nomre = db.Column(db.String(100),nullable=False)
    adress = db.Column(db.String(100),nullable=False)
    magazadi = db.Column(db.String(100),nullable=False)
    seher = db.Column(db.String(100),nullable=False)
    zip = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)
    price = db.Column(db.String,nullable=False)
    quantity = db.Column(db.String,nullable=False)
    total = db.Column(db.String,nullable=False)

class Related(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)
    price = db.Column(db.String,nullable=False)
    quantity = db.Column(db.String,nullable=False)
    total = db.Column(db.String,nullable=False)

class Wishlistrelated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)





class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nike = db.Column(db.String,nullable=False)
    adidas = db.Column(db.String,nullable=False)
    merrel = db.Column(db.String,nullable=False)
    gucci = db.Column(db.String,nullable=False)
    sheckhers = db.Column(db.String,nullable=False)
    product = db.relationship('Productdetail',backref='brand',lazy=True)
   
class Productdetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.String,nullable=False)
    text = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)
    span = db.Column(db.String,nullable=False)
    brand_id = db.Column(db.Integer,db.ForeignKey('brand.id'),nullable=False)




