from abc import ABC, abstractmethod

from domain import db_session
from domain.user import User


class IUsersRepository(ABC):  # интерфейс для репозитория пользователей
    @abstractmethod
    def get_all(self):  # получить всех пользователей
        pass

    @abstractmethod
    def get_user(self, user_id: int):  # получить пользователя
        pass

    @abstractmethod
    def add(self, user: User):  # добавить пользователя
        pass

    @abstractmethod
    def update(self, user_id: int, new_user: User):  # изменить пользователя
        pass

    @abstractmethod
    def delete(self, user_id: int):  # удалить пользователя
        pass


class UsersRepositorySQLAlchemy(IUsersRepository):  # репзиторий пользователей ОРМ SQLAlchemy
    def get_all(self):  # получить всех пользователей
        new_db_session = db_session.create_session()
        return new_db_session.query(User).all()

    def get_user(self, user_id: int):  # получить пользователя
        new_db_session = db_session.create_session()
        return new_db_session.query(User).filter(User.id == user_id).first()

    def add(self, user: User):  # добавить пользователя
        new_db_session = db_session.create_session()
        new_db_session.add(user)
        new_db_session.commit()

    def update(self, user_id: int, new_user: User):  # изменить пользователя
        new_db_session = db_session.create_session()
        user = new_db_session.query(User).filter(User.id == user_id).first()
        user.login = new_user.login
        user.password = new_user.password
        user.email = new_user.email
        user.role_id = new_user.role_id
        new_db_session.commit()

    def delete(self, user_id: int):  # удалить пользователя
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(User).filter(User.id == user_id).first())
        new_db_session.commit()
