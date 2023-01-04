"""Flask app for Cupcakes"""

from flask import Flask, render_template, request, jsonify

from models import db, connect_db, Cupcake

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

connect_db(app)

@app.route('/')
def root():
    '''Create homepage'''

    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    '''Show all cupcakes in db'''

    cupcakes = []cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)


@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    '''Add a cupcake and return data'''

    data = request.jsonify

    cupcake = Cupcake(
        flavor = data['flavor'],
        rating = data['rating'],
        size = data['size'],
        image = data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake = cupcake.to_dict()), 201)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    '''Get data on specific cupcake'''

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['PATCH'])
def update_cupcake(cupcake_id):
    '''Update cupcake data'''

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    sb.session.commit()

    return jsonify(cupcake = cupcake.to_dict())

@app.route('/api/cupcake/<int:cupcake_id>', methods = ['DELETE'])
def remove_cupcake(cupcake_id):
    '''Delete cupcake and send message confirming deletion'''

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = 'Cupcake deleted')


