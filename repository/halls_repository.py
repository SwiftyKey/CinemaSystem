from abc import ABC, abstractmethod

from domain import db_session
from domain.hall import Hall


class IHallsRepository(ABC):  # интерфейс для репозитория залов
    @abstractmethod
    def get_all(self):  # получить все залы
        pass

    @abstractmethod
    def get_hall(self, hall_id: int):  # получить зал
        pass

    @abstractmethod
    def add(self, hall: Hall):  # добавить зал
        pass

    @abstractmethod
    def update(self, hall_id: int, new_hall: Hall):  # изменить зал
        pass

    @abstractmethod
    def delete(self, hall_id: int):  # удалить зал
        pass


class HallsRepositorySQLAlchemy(IHallsRepository):  # репзиторий залов ОРМ SQLAlchemy
    def get_all(self):  # получить все залы
        new_db_session = db_session.create_session()
        return new_db_session.query(Hall).all()

    def get_hall(self, hall_id: int):  # получить зал
        new_db_session = db_session.create_session()
        return new_db_session.query(Hall).filter(Hall.id == hall_id).first()

    def add(self, hall: Hall):  # добавить зал
        new_db_session = db_session.create_session()
        new_db_session.add(hall)
        new_db_session.commit()

    def update(self, hall_id: int, new_hall: Hall):  # изменить зал
        new_db_session = db_session.create_session()
        hall = new_db_session.query(Hall).filter(Hall.id == hall_id).first()
        hall.title = new_hall.title
        hall.cinema_id = new_hall.cinema_id
        new_db_session.commit()

    def delete(self, hall_id: int):  # удалить зал
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Hall).filter(Hall.id == hall_id).first())
        new_db_session.commit()
