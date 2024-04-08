from flask_restful import Resource

from services.tickets_service import TicketService


class TicketResource(Resource):  # контроллер для работы с одним билетом
    ticket_service = TicketService()

    def get(self, ticket_id):  # получить
        return self.ticket_service.get_ticket(ticket_id)

    def post(self, ticket):  # добавить
        return self.ticket_service.add(ticket)

    def put(self, ticket_id, ticket):  # изменить
        return self.ticket_service.update(ticket_id, ticket)

    def delete(self, ticket_id):  # удалить
        return self.ticket_service.delete(ticket_id)


class TicketsListResources(Resource):  # контроллер для работы со списком билетов
    ticket_service = TicketService()

    def get(self):  # получить
        return self.ticket_service.get_all()
