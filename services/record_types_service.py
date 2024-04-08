from repository.record_types_repository import RecordTypesRepositorySQLAlchemy


class RecordTypeService:  # сервис для общения с репозиторием типов записей
    record_types_repository = RecordTypesRepositorySQLAlchemy()

    def get_all(self):  # получить все типы записей
        return {"record_types": [item.to_dict(only=("id", "title"))
                                 for item in self.record_types_repository.get_all()]}

    def get_record_type(self, record_type_id):  # получить один тип записи
        record_type = self.record_types_repository.get_record_type(record_type_id)
        if record_type:
            return {"record_type": [{"id": record_type.id, "title": record_type.title}]}
        return {"error": "not found"}
