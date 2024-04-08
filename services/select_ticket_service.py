from controllers.chair_controller import ChairResource
from controllers.record_controller import RecordListResources
from controllers.session_controller import SessionResource
from controllers.ticket_controller import TicketsListResources


class SelectTicketService:  # сервис для фильтрации билетов по залу и сессии
    ticket_resource = TicketsListResources()
    chair_resource = ChairResource()
    session_resource = SessionResource()
    record_resource = RecordListResources()

    def select_ticket(self, hall_id, session_id):  # отфильтровать билеты
        busy_tickets = [record["ticket_id"] for record in self.record_resource.get()["records"]]
        tickets = list(filter(lambda ticket:
                              self.chair_resource.get(
                                  ticket["chair_id"])["chair"][0]["hall_id"] == hall_id
                              and ticket["id"] not in busy_tickets,
                              [ticket for ticket in self.ticket_resource.get()["tickets"]
                               if ticket["session_id"] == session_id]))
        for ticket in tickets:
            chair = self.chair_resource.get(ticket["chair_id"])["chair"][0]
            ticket["row"] = chair["row"]
            ticket["place"] = chair["place"]
        tickets.sort(key=lambda x: (x["row"], x["place"]))
        return {"tickets": tickets}
