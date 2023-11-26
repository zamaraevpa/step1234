import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

if "SQL_DATABASE_TYPE" in os.environ and os.environ["SQL_DATABASE_TYPE"] == "postgres":
    app.config["SQLALCHEMY_DATABASE_URI"] = get_postgres_database_uri()
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

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

def get_postgres_database_uri():
    sql_user = os.environ["SQL_USER"]
    sql_password = os.environ["SQL_PASSWORD"]
    sql_host = os.environ["SQL_HOST"]
    sql_port = os.environ["SQL_PORT"]
    sql_database = os.environ["SQL_DATABASE"]
    return f"postgresql://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"
