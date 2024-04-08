from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from domain.hall_session import hall_session_table
from sqlalchemy_serializer import SerializerMixin


class Session(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей сессий
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_datetime = Column(DateTime, nullable=False)

    film_id = Column('film_id', Integer, ForeignKey('films.id'), nullable=False)
    film = relationship('Film', back_populates='session')

    halls = relationship("Hall", secondary=hall_session_table, back_populates='session')

    cost = relationship("Cost")

    ticket = relationship("Ticket")
