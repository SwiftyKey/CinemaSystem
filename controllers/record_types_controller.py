from flask_restful import Resource

from services.record_types_service import RecordTypeService


class RecordTypesResource(Resource):  # контроллер для работы с одним типом записи
    record_type_service = RecordTypeService()

    def get(self, record_type_id):  # получить
        return self.record_type_service.get_record_type(record_type_id)


class RecordTypesListResources(Resource):  # контроллер для работы со списком типов записей
    record_type_service = RecordTypeService()

    def get(self):  # получить
        return self.record_type_service.get_all()
