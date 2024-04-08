from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Cinema(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей кинотеатров
    __tablename__ = "cinemas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    hall = relationship("Hall")
