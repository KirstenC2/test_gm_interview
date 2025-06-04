from flask_sqlalchemy import SQLAlchemy
from db_conn import database
from sqlalchemy.dialects.mysql import JSON

class Item(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    code = database.Column(database.String(100))
    category = database.Column(database.String(100))
    size = database.Column(database.JSON)  # assuming list stored as JSON
    unit_price = database.Column(database.Float)
    inventory = database.Column(database.Integer)
    color = database.Column(database.JSON)  # assuming list stored as JSON

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'category': self.category,
            'size': self.size,
            'unit_price': self.unit_price,
            'inventory': self.inventory,
            'color': self.color
        }
