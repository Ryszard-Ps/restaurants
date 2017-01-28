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
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)

        data, errors = schema.load(json_data)
        print(data)
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



api.add_resource(RestaurantsList, '')
