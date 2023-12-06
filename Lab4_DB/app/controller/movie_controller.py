from .general_controller import GeneralController
from ..service import movie_service


class MovieController(GeneralController):
    _service = movie_service
