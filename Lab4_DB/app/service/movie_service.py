from .general_service import GeneralService
from ..dao import movie_dao


class MovieService(GeneralService):
    _dao = movie_dao
