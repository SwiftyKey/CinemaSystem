from abc import ABC, abstractmethod

from domain import db_session
from domain.session import Session


class ISessionsRepository(ABC):  # интерфейс для репозитория сессий
    @abstractmethod
    def get_all(self):  # получить все сессии
        pass

    @abstractmethod
    def get_session(self, session_id: int):  # получить сессию
        pass

    @abstractmethod
    def add(self, session: Session):  # добавить сессию
        pass

    @abstractmethod
    def update(self, session_id: int, new_session: Session):  # изменить сессию
        pass

    @abstractmethod
    def delete(self, session_id: int):  # удалить сессию
        pass


class SessionsRepositorySQLAlchemy(ISessionsRepository):  # репзиторий сессий ОРМ SQLAlchemy
    def get_all(self):  # получить все сессии
        new_db_session = db_session.create_session()
        return new_db_session.query(Session).all()

    def get_session(self, session_id: int):  # получить сессию
        new_db_session = db_session.create_session()
        return new_db_session.query(Session).filter(Session.id == session_id).first()

    def add(self, session: Session):  # добавить сессию
        new_db_session = db_session.create_session()
        new_db_session.add(session)
        new_db_session.commit()

    def update(self, session_id: int, new_session: Session):  # изменить сессию
        new_db_session = db_session.create_session()
        session = new_db_session.query(Session).filter(Session.id == session_id).first()
        session.film_id = new_session.film_id
        session.session_datetime = new_session.session_datetime
        new_db_session.commit()

    def delete(self, session_id: int):  # удалить сессию
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Session).filter(Session.id == session_id).first())
        new_db_session.commit()
