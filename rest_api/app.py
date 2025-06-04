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


    @app.route('/Items/<int:item_id>', methods=['GET'])
    def get_item_by_id(item_id):
        item = Item.query.filter_by(id=item_id).first()
        if item:
            return jsonify(item.to_dict())
        else:
            return jsonify({'error': 'Item not found'}), 404

    @app.route('/Items', methods=['GET'])
    def get_all_items():
        items = Item.query.all()
        return jsonify([item.to_dict() for item in items])



    @app.route('/Items/<int:item_id>', methods=['PUT'])
    def update_item(item_id):
        data = request.get_json()
        item = Item.query.filter_by(id=item_id).first()

        if item:
            item.name = data.get('name', item.name)
            item.category = data.get('category', item.category)
            item.size = data.get('size', item.size)
            item.unit_price = data.get('unit_price', item.unit_price)
            item.inventory = data.get('inventory', item.inventory)
            item.color = data.get('color', item.color)

            database.session.commit()
            return jsonify(item.to_dict())
        else:
            return jsonify({'error': 'Item not found'}), 404



    @app.route('/Items/<int:item_id>', methods=['DELETE'])
    def delete_item(item_id):
        item = Item.query.filter_by(id=item_id).first()
        if item:
            database.session.delete(item)
            database.session.commit()
            return jsonify({'message': 'Item deleted'})
        else:
            return jsonify({'error': 'Item not found'}), 404


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8081)
