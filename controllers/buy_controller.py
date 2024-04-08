from services.buy_service import BuyService


class BuyResource:  # контроллер для работы с функционалом покупки билетов
    buy_service = BuyService()

    def buy(self, ticket_id: int):  # покупка
        self.buy_service.buy(ticket_id)
