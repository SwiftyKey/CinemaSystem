from datetime import datetime

from flask_login import current_user

from controllers.record_controller import RecordResource
from domain.record import Record


class BuyService:  # сервис для создание записей покупки билетов
    record_resource = RecordResource()

    def buy(self, ticket_id: int):  # купить
        self.record_resource.post(Record(user_id=current_user.id, ticket_id=ticket_id,
                                         purchase_date=datetime.now(), record_type_id=1))
