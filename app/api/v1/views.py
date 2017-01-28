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
        data, errors = schema.load(json_data)
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


class RestaurantsDetail(Resource):
    def get(self, id):
        query_set = Restaurants.query.get(id)
        res = schema.dump(query_set).data
        res.status_code = 200
        return res

    def put(self, id):
        json_data = request.get_json(force=True)
        data, errors = schema.load(json_data)
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

    def delete(self, id):
        restaurant = Restaurants.query.get(id)
        delete = restaurant.delete(restaurant)
        res = make_response()
        res.status_code = 204
        return res


api.add_resource(RestaurantsList, '')
api.add_resource(RestaurantsDetail, '/<string:id>')
