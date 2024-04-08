from abc import ABC, abstractmethod

from domain import db_session
from domain.role import Role


class IRolesRepository(ABC):  # интерфейс для репозитория ролей
    @abstractmethod
    def get_all(self):  # получить все роли
        pass

    @abstractmethod
    def get_role(self, role_id: Role):  # получить роль
        pass


class RolesRepositorySQLAlchemy(IRolesRepository):  # репзиторий ролей ОРМ SQLAlchemy
    def get_all(self):  # получить все роли
        new_db_session = db_session.create_session()
        return new_db_session.query(Role).all()

    def get_role(self, role_id: Role):  # получить роль
        new_db_session = db_session.create_session()
        return new_db_session.query(Role).filter(Role.id == role_id).first()
