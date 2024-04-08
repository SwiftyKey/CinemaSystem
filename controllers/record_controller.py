from flask_restful import Resource

from services.records_service import RecordsService


class RecordResource(Resource):  # контроллер для работы с одной записью
    record_service = RecordsService()

    def get(self, record_id):  # получить
        return self.record_service.get_record(record_id)

    def post(self, record):  # добавить
        return self.record_service.add(record)

    def put(self, record_id, record):  # изменить
        return self.record_service.update(record_id, record)

    def delete(self, record_id):  # удалить
        return self.record_service.delete(record_id)


class RecordListResources(Resource):  # контроллер для работы со списком записей
    record_service = RecordsService()

    def get(self):  # получить
        return self.record_service.get_all()
