import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

sql_user = os.environ["SQL_USER"]
sql_password = os.environ["SQL_PASSWORD"]
sql_host = os.environ["SQL_HOST"]
sql_port = os.environ["SQL_PORT"]
sql_database = os.environ["SQL_DATABASE"]

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"
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