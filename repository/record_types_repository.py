from abc import ABC, abstractmethod

from domain import db_session
from domain.record_type import RecordType


class IRecordTypesRepository(ABC):  # интерфейс для типов записей
    @abstractmethod
    def get_all(self):  # получить все типы записей
        pass

    @abstractmethod
    def get_record_type(self, record_type_id: RecordType):  # получить тип записи
        pass


# репзиторий типов записей ОРМ SQLAlchemy
class RecordTypesRepositorySQLAlchemy(IRecordTypesRepository):
    def get_all(self):  # получить все типы записей
        new_db_session = db_session.create_session()
        return new_db_session.query(RecordType).all()

    def get_record_type(self, record_type_id: RecordType):  # получить тип записи
        new_db_session = db_session.create_session()
        return new_db_session.query(RecordType).filter(RecordType.id == record_type_id).first()
