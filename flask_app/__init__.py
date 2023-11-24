import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@postgres_ip:5432/postgres_db"
app.config["SECRET_KEY"] = secrets.token_hex()

db.init_app(app)

from . import models

with app.app_context():
    db.create_all()

from . import auth
app.register_blueprint(auth.bp)

from . import views
app.register_blueprint(views.bp)
app.add_url_rule('/', endpoint='index')