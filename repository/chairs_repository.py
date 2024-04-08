from abc import ABC, abstractmethod

from domain import db_session
from domain.chair import Chair


class IChairsRepository(ABC):  # интерфейс для репозитория стульев
    @abstractmethod
    def get_all(self):  # получить все стулья
        pass

    @abstractmethod
    def get_chair(self, chair_id: int):  # получить стул
        pass

    @abstractmethod
    def add(self, chair: Chair):  # добавить стул
        pass

    @abstractmethod
    def update(self, chair_id: int, new_chair: Chair):  # изменить стул
        pass

    @abstractmethod
    def delete(self, chair_id: int):  # удалить стул
        pass


class ChairsRepositorySQLAlchemy(IChairsRepository):  # репзиторий стульев ОРМ SQLAlchemy
    def get_all(self):  # получить все стулья
        new_db_session = db_session.create_session()
        return new_db_session.query(Chair).all()

    def get_chair(self, chair_id: int):  # получить стул
        new_db_session = db_session.create_session()
        return new_db_session.query(Chair).filter(Chair.id == chair_id).first()

    def add(self, chair: Chair):  # добавить стул
        new_db_session = db_session.create_session()
        new_db_session.add(chair)
        new_db_session.commit()

    def update(self, chair_id: int, new_chair: Chair):  # изменить стул
        new_db_session = db_session.create_session()
        chair = new_db_session.query(Chair).filter(Chair.id == chair_id).first()
        chair.row = new_chair.row
        chair.place = new_chair.place
        chair.hall_id = new_chair.hall_id
        new_db_session.commit()

    def delete(self, chair_id: int):  # удалить стул
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Chair).filter(Chair.id == chair_id).first())
        new_db_session.commit()
