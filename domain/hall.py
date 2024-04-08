from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from domain.hall_session import hall_session_table
from sqlalchemy_serializer import SerializerMixin


class Hall(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей залов
    __tablename__ = "halls"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    cinema_id = Column("cinema_id", Integer, ForeignKey('cinemas.id'), nullable=False)
    cinema = relationship("Cinema", back_populates='hall')

    session = relationship("Session", secondary=hall_session_table, back_populates='halls')

    chair = relationship("Chair")
