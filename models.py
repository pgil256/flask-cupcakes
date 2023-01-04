"""Models for Cupcake app."""

from flask_sqlalchemu import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = 'https://media.istockphoto.com/id/177047298/photo/vanilla-cupcakes-with-pink-yellow-and-blue-icing-isolated.jpg?s=612x612&w=0&k=20&c=JfKDY3kL7prAt0NJ0efXIV8xn51_lJuIEctxDfdYXqU='


class Cupcake(db.Model):
    '''Defines instance of cupcake'''

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, default = DEFAULT_IMG)

    def to dict(self):
        'Serialize cupcake to a sict of cupcake info'

        return {
            'id': self.id,
            'flavor': self.flavor.
            'rating': self.rating,
            'size': self.size,
            'image': self.image
        }

def connect_db(app):
    '''Connect to db'''

    db.app = app
    db.init_app(app)