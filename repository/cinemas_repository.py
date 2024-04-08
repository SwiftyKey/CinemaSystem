from abc import ABC, abstractmethod

from domain import db_session
from domain.cinema import Cinema


class ICinemasRepository(ABC):  # интерфейс для репозитория кинотеатров
    @abstractmethod
    def get_all(self):  # получить все кинотеатры
        pass

    @abstractmethod
    def get_cinema(self, cinema_id: int):  # получить кинотеатр
        pass

    @abstractmethod
    def add(self, cinema: Cinema):  # добавить кинотеатр
        pass

    @abstractmethod
    def update(self, cinema_id: int, new_cinema: Cinema):  # изменить кинотеатр
        pass

    @abstractmethod
    def delete(self, cinema_id: int):  # удалить кинотеатр
        pass


class CinemasRepositorySQLAlchemy(ICinemasRepository):  # репзиторий кинотеатров ОРМ SQLAlchemy
    def get_all(self):  # получить все кинотеатры
        new_db_session = db_session.create_session()
        return new_db_session.query(Cinema).all()

    def get_cinema(self, cinema_id: int):  # получить кинотеатр
        new_db_session = db_session.create_session()
        return new_db_session.query(Cinema).filter(Cinema.id == cinema_id).first()

    def add(self, cinema: Cinema):  # добавить кинотеатр
        new_db_session = db_session.create_session()
        new_db_session.add(cinema)
        new_db_session.commit()

    def update(self, cinema_id: int, new_cinema: Cinema):  # изменить кинотеатр
        new_db_session = db_session.create_session()
        cinema = new_db_session.query(Cinema).filter(Cinema.id == cinema_id).first()
        cinema.title = new_cinema.title
        new_db_session.commit()

    def delete(self, cinema_id: int):  # удалить кинотеатр
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Cinema).filter(Cinema.id == cinema_id).first())
        new_db_session.commit()
