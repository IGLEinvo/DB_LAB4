from __future__ import annotations
from typing import Dict, Any
from app import db


class BoxOffice(db.Model):
    __tablename__ = 'BoxOffice'
    box_office_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(45), nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.movie_id'), nullable=False)

    def __repr__(self) -> str:
        return f"BoxOffice({self.box_office_id}, '{self.country}', {self.revenue}, {self.movie_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'box_office_id': self.box_office_id,
            'country': self.country,
            'revenue': self.revenue,
            'movie_id': self.movie_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BoxOffice:
        box_office = BoxOffice(
            country=dto_dict.get('country'),
            revenue=dto_dict.get('revenue'),
            movie_id=dto_dict.get('movie_id')
        )
        return box_office
