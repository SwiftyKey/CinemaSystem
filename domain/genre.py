from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Genre(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей жанров
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, index=True, nullable=False)

    film = relationship('Film')
