from .general_dao import GeneralDAO
from ..domain import Movie


class MovieDAO(GeneralDAO):
    _domain_type = Movie
