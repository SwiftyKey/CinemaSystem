from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Ticket(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей билетов
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)

    chair_id = Column("chair_id", Integer, ForeignKey('chairs.id'), nullable=False)
    chair = relationship("Chair", back_populates='ticket')

    session_id = Column("session_id", Integer, ForeignKey('sessions.id'), nullable=False)
    session = relationship("Session", back_populates='ticket')

    record = relationship("Record")
