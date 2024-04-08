from flask_restful import Resource

from services.select_ticket_service import SelectTicketService


class SelectTicketResource(Resource):  # контроллер для работы с фукнционалом выбора билетов
    select_ticket_service = SelectTicketService()

    def get(self, hall_id, session_id):  # получить
        return self.select_ticket_service.select_ticket(hall_id, session_id)
