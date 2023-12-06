from .general_controller import GeneralController
from ..service import boxoffice_service


class BoxOfficeController(GeneralController):
    _service = boxoffice_service
