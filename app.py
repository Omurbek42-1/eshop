from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

# Словари для хранения данных
directors = {}
movies = {}
reviews = {}

# Идентификаторы для новых записей
director_id_counter = 1
movie_id_counter = 1
review_id_counter = 1

# Ресурс для работы с режиссерами
class DirectorResource(Resource):
    def get(self, id):
        if id not in directors:
            abort(404, message="Director not found")
        return jsonify(directors[id])

    def post(self):
        global director_id_counter
        data = request.get_json()
        data['id'] = director_id_counter
        directors[director_id_counter] = data
        director_id_counter += 1
        return jsonify(data), 201

    def put(self, id):
        if id not in directors:
            abort(404, message="Director not found")
        data = request.get_json()
        data['id'] = id
        directors[id] = data
        return jsonify(data)

    def delete(self, id):
        if id not in directors:
            abort(404, message="Director not found")
        del directors[id]
        return '', 204

# Ресурс для работы с фильмами
class MovieResource(Resource):
    def get(self, id):
        if id not in movies:
            abort(404, message="Movie not found")
        return jsonify(movies[id])

    def post(self):
        global movie_id_counter
        data = request.get_json()
        data['id'] = movie_id_counter
        movies[movie_id_counter] = data
        movie_id_counter += 1
        return jsonify(data), 201

    def put(self, id):
        if id not in movies:
            abort(404, message="Movie not found")
        data = request.get_json()
        data['id'] = id
        movies[id] = data
        return jsonify(data)

    def delete(self, id):
        if id not in movies:
            abort(404, message="Movie not found")
        del movies[id]
        return '', 204

# Ресурс для работы с отзывами
class ReviewResource(Resource):
    def get(self, id):
        if id not in reviews:
            abort(404, message="Review not found")
        return jsonify(reviews[id])

    def post(self):
        global review_id_counter
        data = request.get_json()
        data['id'] = review_id_counter
        reviews[review_id_counter] = data
        review_id_counter += 1
        return jsonify(data), 201

    def put(self, id):
        if id not in reviews:
            abort(404, message="Review not found")
        data = request.get_json()
        data['id'] = id
        reviews[id] = data
        return jsonify(data)

    def delete(self, id):
        if id not in reviews:
            abort(404, message="Review not found")
        del reviews[id]
        return '', 204

# Добавляем ресурсы к API
api.add_resource(DirectorResource, '/api/v1/directors/', '/api/v1/directors/<int:id>')
api.add_resource(MovieResource, '/api/v1/movies/', '/api/v1/movies/<int:id>')
api.add_resource(ReviewResource, '/api/v1/reviews/', '/api/v1/reviews/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
