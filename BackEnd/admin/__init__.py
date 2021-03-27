from web import app
from admin.routes import admin_bp

app.register_blueprint(admin_bp)