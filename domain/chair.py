from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Chair(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей стульев
    __tablename__ = "chairs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    row = Column(Integer, nullable=False)
    place = Column(Integer, nullable=False)

    hall_id = Column("hall_id", Integer, ForeignKey('halls.id'), nullable=False)
    hall = relationship("Hall", back_populates='chair')

    ticket = relationship("Ticket")
