from abc import ABC, abstractmethod

from domain import db_session
from domain.ticket import Ticket


class ITicketsRepository(ABC):  # интерфейс для репозитория билетов
    @abstractmethod
    def get_all(self):  # получить все билеты
        pass

    @abstractmethod
    def get_ticket(self, ticket_id: int):  # получить билет
        pass

    @abstractmethod
    def add(self, ticket: Ticket):  # добавить билет
        pass

    @abstractmethod
    def update(self, ticket_id: int, new_ticket: Ticket):  # изменить билет
        pass

    @abstractmethod
    def delete(self, ticket_id: int):  # удалить билет
        pass


class TicketsRepositorySQLAlchemy(ITicketsRepository):  # репзиторий билетов ОРМ SQLAlchemy
    def get_all(self):  # получить все билеты
        new_db_session = db_session.create_session()
        return new_db_session.query(Ticket).all()

    def get_ticket(self, ticket_id: int):  # получить билет
        new_db_session = db_session.create_session()
        return new_db_session.query(Ticket).filter(Ticket.id == ticket_id).first()

    def add(self, ticket: Ticket):  # добавить билет
        new_db_session = db_session.create_session()
        new_db_session.add(ticket)
        new_db_session.commit()

    def update(self, ticket_id: int, new_ticket: Ticket):  # изменить билет
        new_db_session = db_session.create_session()
        ticket = new_db_session.query(Ticket).filter(Ticket.id == ticket_id).first()
        ticket.number = new_ticket.number
        ticket.cost = new_ticket.cost
        ticket.chair_id = new_ticket.chair_id
        ticket.session_id = new_ticket.session_id
        new_db_session.commit()

    def delete(self, ticket_id: int):  # удалить билет
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Ticket).filter(Ticket.id == ticket_id).first())
        new_db_session.commit()
