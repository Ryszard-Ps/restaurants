from flask import Blueprint, request, make_response
from api.v1.models import Restaurants, RestaurantsSchema, db
from flask_restful import Api, Resource

restaurants = Blueprint('restaurants', __name__)
schema = RestaurantsSchema()
api = Api(restaurants)


class RestaurantsList(Resource):
    def get(self):
        query_set = Restaurants.query.all()
        res = schema.dump(query_set, many=True).data
        return res, 200

api.add_resource(RestaurantsList, '')
