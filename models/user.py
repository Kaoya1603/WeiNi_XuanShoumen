import sqlalchemy
from data.db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    country = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    region = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    grade = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
