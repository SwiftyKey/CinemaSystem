from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Record(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей записей
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_date = Column(DateTime, nullable=False)

    record_type_id = Column("record_type_id", Integer, ForeignKey("record_types.id"), nullable=False)
    record_type = relationship("RecordType", back_populates='record')

    ticket_id = Column("ticket_id", Integer, ForeignKey("tickets.id"), nullable=False)
    ticket = relationship("Ticket", back_populates='record')

    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates='record')
