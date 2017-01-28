from marshmallow import Schema, fields, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from collections import OrderedDict
from api import db


class Restaurants(db.Model):
    id = db.Column(db.TEXT, primary_key=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.TEXT)
    site = db.Column(db.TEXT)
    street = db.Column(db.TEXT)
    city = db.Column(db.TEXT)
    state = db.Column(db.TEXT)
    lat = db.Column(db.TEXT)
    lng = db.Column(db.TEXT)


    def __init__(self,  rating, name, site, street, city, state, lat, lng):
        self.rating = rating
        self.name = name
        self.site = site
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng

class RestaurantsSchema(Schema):

    id = fields.String(dump_only=True)
    rating = fields.Integer()
    name = fields.String()
    site = fields.String()
    street = fields.String()
    city = fields.String()
    state = fields.String()
    lat = fields.String()
    lng = fields.String()

    class Meta:
        type_ = 'restaurants'
        fields = ("id", "rating", "name", "site", "street", "city", "state", "lat", "lng")
        ordered = True
