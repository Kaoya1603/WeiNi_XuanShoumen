import sqlalchemy
from data.db_session import SqlAlchemyBase


class Favorite(SqlAlchemyBase):
    __tablename__ = 'favorites'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    competition = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    orientation = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("orientations.id"), nullable=False)
    profile = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    subject = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    level = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    register = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    send_alerts = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
