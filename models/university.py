import sqlalchemy
from data.db_session import SqlAlchemyBase


class University(SqlAlchemyBase):
    __tablename__ = 'universities'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    university = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    competition = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    profile = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    subject = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    exam_scores = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    privilege = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    status = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    grade = sqlalchemy.Column(sqlalchemy.String, nullable=False)
