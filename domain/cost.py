from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Cost(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей цен
    __tablename__ = "costs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cost = Column(Float, nullable=False)

    session_id = Column('session_id', Integer, ForeignKey('sessions.id'), nullable=False)
    session = relationship("Session", back_populates='cost')
