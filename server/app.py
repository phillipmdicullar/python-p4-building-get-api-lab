#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'


@app.route('/bakeries')
def bakeries():
    # bakes =  [bakery.to_dict() for bakery in Bakery.query.all()]
    # return make_response(bakes, 200)
    bakes = [bakes.to_dict() for bakes in Bakery.query.all()]
    return make_response(bakes, 200)
@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakes = Bakery.query.filter(Bakery.id == id).first()
    return make_response(bakes.to_dict(), 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bakes = [bake.to_dict() for bake in BakedGood.query.order_by(BakedGood.price.desc()).all()]
    return make_response(bakes, 200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    expensive = BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first()
    most_expensive_changer = expensive.to_dict()
    return make_response( most_expensive_changer,   200  )

if __name__ == '__main__':
    app.run(port=5555, debug=True)
