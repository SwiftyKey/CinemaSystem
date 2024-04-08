from abc import ABC, abstractmethod

from domain import db_session
from domain.hall import Hall
from domain.hall_session import hall_session_table
from domain.session import Session


class IHallsSessionsRepository(ABC):  # интерфейс для репозитория залов-сессий
    @abstractmethod
    def get_all(self):  # получить все залы-сессии
        pass

    @abstractmethod
    def get_hall_sessions(self, hall_id: int):  # получить зал-сессию
        pass

    @abstractmethod
    def add(self, hall: Hall, session: Session):  # добавить зал-сессию
        pass

    @abstractmethod
    def update(self, hall: Hall, session: Session, new_session: Session):  # изменить зал-сессию
        pass

    @abstractmethod
    def delete(self, hall: Hall, session: Session):  # удалить зал-сессию
        pass


# репзиторий залов-сессий ОРМ SQLAlchemy
class HallsSessionsRepositorySQLAlchemy(IHallsSessionsRepository):
    def get_all(self):  # получить все залы-сессии
        new_db_session = db_session.create_session()
        return new_db_session.query(hall_session_table).all()

    def get_hall_sessions(self, hall_id: int):  # получить зал-сессию
        new_db_session = db_session.create_session()
        return new_db_session.query(hall_session_table).filter(
            hall_session_table.hall_id == hall_id).all()

    def add(self, hall: Hall, session: Session):  # добавить зал-сессию
        new_db_session = db_session.create_session()
        hall.session.append(session)
        new_db_session.commit()

    def update(self, hall: Hall, session: Session, new_session: Session):  # изменить зал-сессию
        new_db_session = db_session.create_session()
        hall.session.remove(session)
        hall.session.append(new_session)
        new_db_session.commit()

    def delete(self, hall: Hall, session: Session):  # удалить зал-сессию
        new_db_session = db_session.create_session()
        hall.session.remove(session)
        new_db_session.commit()
