from flask_sqlalchemy import SQLAlchemy
from db_conn import database
from sqlalchemy.dialects.mysql import JSON

class Item(database.Model):
    __table_name__ = "inventory"
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50), nullable = False)
    code = database.Column(database.String(15), nullable = False)
    category = database.Column(database.String(15), nullable = False)
    size = database.Column(JSON,nullable = False)
    unit_price = database.Column(database.Integer, nullable = False)
    inventory = database.Column(database.Integer, nullable = False)
    color = database.Column(JSON,nullable = False)