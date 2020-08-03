from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, CHAR, BYTEA

from utils import database


class User(UserMixin, database.Model):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    login = Column(CHAR(60), unique=True, nullable=False)
    password = Column(BYTEA, unique=False, nullable=False)
    email = Column(CHAR(60), unique=True, nullable=False)
    followed_channels = Column(CHAR, unique=False, nullable=True)

    def register_new_user(self):
        check_email_already_exist = self.query.filter_by(email=self.email).first()
        if check_email_already_exist:
            return {"success": False, "message": "This email is already used"}

        check_login_already_exist = self.query.filter_by(login=self.login).first()
        if check_login_already_exist:
            return {"success": False, "message": "This login is already used"}

        database.session.add(self)
        database.session.commit()
        return {"success": True}

    def get_followed_channels(self):
        pass

    def __repr__(self):
        return f"User data: (login: {self.login}, email: {self.email}, followed channels: {self.followed_channels})."
