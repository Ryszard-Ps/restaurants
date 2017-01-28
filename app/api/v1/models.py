# -*- encoding: utf-8 -*-
from marshmallow import Schema, fields, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from collections import OrderedDict
from api import db

class DAO():
    """Ejecuta los cambios del recurso Restaurants."""
    def add(self, resource):
        """Realiza la creación del recurso Restaurants.

        Argumentos:
        resource - Objeto del tipo Restaurants
        """
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        """Realiza la actualización del recurso Restaurants."""
        return db.session.commit()

    def delete(self, resource):
        """Realiza la eliminación del recurso Restaurants.

        Argumentos:
        resource - Objeto del tipo Restaurants
        """

        db.session.delete(resource)
        return db.session.commit()


class Restaurants(db.Model, DAO):
    """Estructura básica del recurso Restaurants."""
    id = db.Column(db.TEXT, primary_key=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.TEXT)
    site = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    street = db.Column(db.TEXT)
    city = db.Column(db.TEXT)
    state = db.Column(db.TEXT)
    lat = db.Column(db.TEXT)
    lng = db.Column(db.TEXT)


    def __init__(
        self,id ,rating, name, site, email, phone, street, city, state, lat, lng
        ):
        """Constructor de Restaurants."""
        self.id = id
        self.rating = rating
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng

class RestaurantsSchema(Schema):
    """Serializador y Deserializador de Restaurants."""
    id = fields.String()
    rating = fields.Integer()
    name = fields.String()
    site = fields.String()
    email = fields.String()
    phone = fields.String()
    street = fields.String()
    city = fields.String()
    state = fields.String()
    lat = fields.String()
    lng = fields.String()

    class Meta:
        type_ = 'restaurants'
        fields = (
            "id", "rating", "name", "site", "email", "phone", "street",
             "city", "state", "lat", "lng"
        )
        ordered = True
