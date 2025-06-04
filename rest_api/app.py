from flask import Flask, request, jsonify
from db_conn import database, init_conn
from models import Item

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test_user:test_password@database:3306/inventory'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)
    init_conn(app)
    @app.route('/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "hello world"}), 200



    @app.route('/Items', methods=['POST'])
    def create_Item():
        data = request.get_json()
        item = Item(
            name=data['name'],
            code=data['code'],
            category=data['category'],
            size=data['size'],
            unit_price=data['unit_price'],
            inventory=data['inventory'],
            color=data['color']
        )
        database.session.add(item)
        database.session.commit()
        return jsonify({"message": "Item created successfully"}), 201


    @app.route('/Items/<code>', methods=['GET'])
    def get_Item(code):
        Item = Item.query.filter_by(code=code).first()
        if not Item:
            return jsonify({'error': 'Not found'}), 404
        return jsonify({
            "name": Item.name,
            "code": Item.code,
            "category": Item.category,
            "size": Item.size,               # Already a list
            "unit_price": Item.unit_price,
            "inventory": Item.inventory,
            "color": Item.color              # Already a list
        })

    @app.route('/Items/<code>', methods=['PUT'])
    def update_Item(code):
        Item = Item.query.filter_by(code=code).first()
        if not Item:
            return jsonify({'error': 'Not found'}), 404
        data = request.json
        Item.name = data['name']
        Item.category = data['category']
        Item.size = data['size']
        Item.unit_price = data['unit_price']
        Item.inventory = data['inventory']
        Item.color = data['color']
        database.session.commit()
        return jsonify(data)

    @app.route('/Items/<code>', methods=['DELETE'])
    def delete_Item(code):
        Item = Item.query.filter_by(code=code).first()
        if not Item:
            return jsonify({'error': 'Not found'}), 404
        database.session.delete(Item)
        database.session.commit()
        return jsonify({'message': 'Deleted'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8081)
