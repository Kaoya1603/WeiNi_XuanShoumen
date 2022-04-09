import sqlalchemy
from data.db_session import SqlAlchemyBase


class Competition(SqlAlchemyBase):
    __tablename__ = 'competitions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    competition = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    orientation = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("orientatios.id"), nullable=False)
    profile = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    subject = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    level = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
