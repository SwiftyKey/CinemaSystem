from flask_login import current_user

from controllers.chair_controller import ChairResource
from controllers.record_controller import RecordListResources
from controllers.record_types_controller import RecordTypesResource
from controllers.ticket_controller import TicketResource


class PersonalAreaService:  # сервис для предоставления данных личного кабинета пользователя
    record_resource = RecordListResources()
    ticket_resource = TicketResource()
    record_type_resource = RecordTypesResource()
    chair_resource = ChairResource()

    def get_user_tickets(self):  # получение билетов пользователя
        records = list(filter(lambda record: record["user_id"] == current_user.id,
                              self.record_resource.get()["records"]))
        tickets = [self.ticket_resource.get(record["ticket_id"])["ticket"][0] for record in records]

        for ticket, record in zip(tickets, records):
            operation = self.record_type_resource.get(record["record_type_id"])["record_type"][0]
            chair = self.chair_resource.get(ticket["chair_id"])["chair"][0]
            ticket["row"] = chair["row"]
            ticket["place"] = chair["place"]
            ticket["purchase_date"] = record["purchase_date"]
            if operation["title"] == "Бронирование":
                ticket["operation"] = "Забронирован"
            else:
                ticket["operation"] = "Куплен"

        return tickets
