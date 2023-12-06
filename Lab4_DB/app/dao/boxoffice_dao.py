from .general_dao import GeneralDAO
from ..domain import BoxOffice


class BoxOfficeDAO(GeneralDAO):
    _domain_type = BoxOffice
