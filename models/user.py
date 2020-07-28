from flask_login import UserMixin
from sqlalchemy import Column, Integer, Binary, String

from utils import database


class User(UserMixin, database.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String(60), unique=True, nullable=False)
    password = Column(Binary, unique=False, nullable=False)
    email = Column(String(60), unique=True, nullable=False)

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def register(self):
        check_email_already_exist = self.query.filter_by(email=self.email).first()
        if check_email_already_exist:
            return {"status": False, "message": "This email is already used"}

        check_login_already_exist = self.query.filter_by(login=self.login).first()
        if check_login_already_exist:
            return {"status": False, "message": "This login is already used"}

        database.session.add(self)
        database.session.commit()
        return {"status": True, "message": "Success"}
