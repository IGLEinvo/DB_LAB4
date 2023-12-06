from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import movie_controller
from ..domain.movie import Movie

movie_bp = Blueprint('movie', __name__, url_prefix='/movie')


@movie_bp.route('', methods=['GET'])
def get_all_movies() -> Response:
    return make_response(jsonify([movie.put_into_dto() for movie in movie_controller.find_all_movies()]), HTTPStatus.OK)


@movie_bp.route('', methods=['POST'])
def create_movie() -> Response:
    content = request.get_json()
    movie = Movie.create_from_dto(content)
    movie_controller.create_movie(movie)
    return make_response(jsonify(movie.put_into_dto()), HTTPStatus.CREATED)


@movie_bp.route('/<int:movie_id>', methods=['GET'])
def get_movie(movie_id: int) -> Response:
    return make_response(jsonify(movie_controller.find_movie_by_id(movie_id)), HTTPStatus.OK)


@movie_bp.route('/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id: int) -> Response:
    content = request.get_json()
    movie = Movie.create_from_dto(content)
    movie_controller.update_movie(movie_id, movie)
    return make_response("Movie updated", HTTPStatus.OK)


@movie_bp.route('/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id: int) -> Response:
    movie_controller.delete_movie(movie_id)
    return make_response("Movie deleted", HTTPStatus.OK)
