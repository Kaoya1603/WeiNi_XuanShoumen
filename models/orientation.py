import sqlalchemy
from data.db_session import SqlAlchemyBase


class Orientation(SqlAlchemyBase):
    __tablename__ = 'orientations'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    orientation = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
