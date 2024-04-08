from repository.tickets_repository import TicketsRepositorySQLAlchemy


class TicketService:  # сервис для общения с репозиторием билетов
    tickets_repository = TicketsRepositorySQLAlchemy()

    def get_all(self):  # получить все билеты
        return {"tickets": [item.to_dict(only=("id", "number", "cost", "chair_id", "session_id"))
                            for item in self.tickets_repository.get_all()]}

    def get_ticket(self, ticket_id):  # получить один билет
        ticket = self.tickets_repository.get_ticket(ticket_id)
        if ticket:
            return {"ticket": [item.to_dict(only=("id", "number", "cost", "chair_id", "session_id"))
                               for item in [ticket]]}
        return {"error": "not found"}

    def add(self, ticket):  # добавить билет
        self.tickets_repository.add(ticket)
        return {"success": "ok"}

    def update(self, ticket_id, ticket):  # изменить существующий билет
        if self.tickets_repository.get_ticket(ticket_id):
            self.tickets_repository.update(ticket_id, ticket)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, ticket_id):  # удалить билет
        if self.tickets_repository.get_ticket(ticket_id):
            self.tickets_repository.delete(ticket_id)
            return {"success": "ok"}
        return {"error": "not found"}
