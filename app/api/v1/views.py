# -*- encoding: utf-8 -*-
from flask import Blueprint, request, make_response, jsonify
from api.v1.models import Restaurants, RestaurantsSchema, db
from flask_restful import Api, Resource

restaurants = Blueprint('restaurants', __name__)
schema = RestaurantsSchema()
api = Api(restaurants)

# Recurso de Restaurants
class RestaurantsList(Resource):
    def get(self):
        """Obtiene un arreglo de Restaurants."""
        try:
            query_set = Restaurants.query.all()
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            raise
    def post(self):
        """Crea un nuevo Restaurant."""
        json_data = request.get_json(force=True)
        if not json_data:
            error = "Información insuficientes."
            return jsonify(error=error)

        data, errors = schema.load(json_data)
        if errors:
            error = "Atributos requeridos"
            return jsonify(error=error)
        try:
            id, rating = data['id'], data['rating']
            name, site = data['name'], data['site']
            email, phone = data['email'], data['phone']
            street, city = data['street'], data['city']
            state, lat, lng = data['state'], data['lat'], data['lng']
            restaurant = Restaurants(
                id=id,
                rating=rating,
                name=name,
                site=site,
                email=email,
                phone=phone,
                street=street,
                city=city,
                state=state,
                lat=lat,
                lng=lng
            )
            restaurant.add(restaurant)
            query = Restaurants.query.get(restaurant.id)
            res = schema.dump(query).data
            return res, 201

        except Exception as e:
            raise


class RestaurantsDetail(Resource):
    def get(self, id):
        """Devuelve al Restaurant con <id>."""
        try:
            query_set = Restaurants.query.get(id)
            if query_set is None:
                error = "Recurso no encontrado"
                return jsonify(error=error)
            else:
                res = schema.dump(query_set).data
                res.status_code = 200
                return res

        except Exception as e:
            raise

    def put(self, id):
        """Actualiza al Restaurant con <id>."""
        json_data = request.get_json(force=True)
        data, errors = schema.load(json_data)
        if errors:
            error = "Atriutos requeridos"
            return jsonify(error=error)
        try:
            restaurant = Restaurants.query.get(id)
            rating = data['rating']
            setattr(restaurant, 'rating',data['rating'])
            setattr(restaurant, 'name', data['name'])
            setattr(restaurant, 'site',data['site'])
            setattr(restaurant, 'email',data['email'])
            setattr(restaurant, 'phone',data['phone'])
            setattr(restaurant, 'street',data['street'])
            setattr(restaurant, 'city',data['city'])
            setattr(restaurant, 'state',data['state'])
            setattr(restaurant, 'lat',data['lat'])
            setattr(restaurant, 'lng',data['lng'])
            restaurant.update()
            return data

        except Exception as e:
            raise

    def delete(self, id):
        """Elimina al Restaurant con <id>."""
        try:
            restaurant = Restaurants.query.get(id)
            delete = restaurant.delete(restaurant)
            res = make_response()
            res.status_code = 204
            return res

        except Exception as e:
            raise

api.add_resource(RestaurantsList, '')
api.add_resource(RestaurantsDetail, '/<string:id>')
