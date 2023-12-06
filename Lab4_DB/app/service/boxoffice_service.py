from .general_service import GeneralService
from ..dao import boxoffice_dao


class BoxOfficeService(GeneralService):
    _dao = boxoffice_dao
