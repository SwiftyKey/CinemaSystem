from abc import ABC, abstractmethod

from domain import db_session
from domain.genre import Genre


class IGenresRepository(ABC):  # интерфейс для репозитория жанров
    @abstractmethod
    def get_all(self):  # получить все жанры
        pass

    @abstractmethod
    def get_genre(self, genre_id: Genre):  # получить жанр
        pass


class GenresRepositorySQLAlchemy(IGenresRepository):  # репзиторий жанров ОРМ SQLAlchemy
    def get_all(self):  # получить все жанры
        new_db_session = db_session.create_session()
        return new_db_session.query(Genre).all()

    def get_genre(self, genre_id: Genre):  # получить жанр
        new_db_session = db_session.create_session()
        return new_db_session.query(Genre).filter(Genre.id == genre_id).first()
