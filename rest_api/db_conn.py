from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def init_conn(app):
    with app.app_context():
        from models import Item
        database.create_all()