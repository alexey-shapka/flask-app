from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import CHAR

from utils import database


class Channel(database.Model):
    __tablename__ = 'channels'

    id = Column(CHAR, primary_key=True, nullable=False)
    title = Column(CHAR, unique=False, nullable=False)
    tag = Column(CHAR, unique=False, nullable=False)
    url = Column(CHAR, unique=False, nullable=True)

    @staticmethod
    def get_popular() -> None:
        return Channel.query.filter_by(tag="popular").all()

    @staticmethod
    def add_channel(id, title: str, tag: str, url: str = None) -> None:
        database.session.add(Channel(id=id, title=title, tag=tag, url=url))
        database.session.commit()

    def __repr__(self) -> str:
        return f"Channel data: (id: {self.id}, title: {self.title}, tag: {self.tag})."
