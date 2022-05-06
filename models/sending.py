import sqlalchemy
from data.db_session import SqlAlchemyBase


class Send(SqlAlchemyBase):
    __tablename__ = 'sending'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, unique=True)
    user_email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    should_send = sqlalchemy.Column(sqlalchemy.Boolean)
