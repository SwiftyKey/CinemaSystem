from abc import ABC, abstractmethod

from domain import db_session
from domain.cost import Cost


class ICostsRepository(ABC):  # интерфейс для репозитория цен
    @abstractmethod
    def get_all(self):  # получить все цены
        pass

    @abstractmethod
    def get_cost(self, cost_id: int):  # получить цену
        pass

    @abstractmethod
    def add(self, cost: Cost):  # добавить цену
        pass

    @abstractmethod
    def update(self, cost_id: int, new_cost: Cost):  # изменить цену
        pass

    @abstractmethod
    def delete(self, cost_id: int):  # удалить цену
        pass


class CostsRepositorySQLAlchemy(ICostsRepository):  # репзиторий цен ОРМ SQLAlchemy
    def get_all(self):  # получить все цены
        new_db_session = db_session.create_session()
        return new_db_session.query(Cost).all()

    def get_cost(self, cost_id: int):  # получить цену
        new_db_session = db_session.create_session()
        return new_db_session.query(Cost).filter(Cost.id == cost_id).first()

    def add(self, cost: Cost):  # добавить цену
        new_db_session = db_session.create_session()
        new_db_session.add(cost)
        new_db_session.commit()

    def update(self, cost_id: int, new_cost: Cost):  # изменить цену
        new_db_session = db_session.create_session()
        cost = new_db_session.query(Cost).filter(Cost.id == cost_id).first()
        cost.cost = new_cost.cost
        cost.session_id = new_cost.session_id
        new_db_session.commit()

    def delete(self, cost_id: int):  # удалить цену
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Cost).filter(Cost.id == cost_id).first())
        new_db_session.commit()
