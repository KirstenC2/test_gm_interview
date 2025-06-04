from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class Item(db.Item):
    __table_name__ = "inventory"
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String, nullable = False)
    code = database.Column(database.String, nullable = False)
    category = database.Column(database.String, nullable = False)
    size = database.Column(database.ARRAY(database.String),nullable = False)
    unit_price = database.Column(database.float, nullable = False)
    inventory = database.Column(database.Integer, nullable = False)
    color = database.Column(database.ARRAY(database.String),nullable = False)