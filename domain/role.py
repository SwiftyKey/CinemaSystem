from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Role(SqlAlchemyBase, SerializerMixin):  # модель для работы с таблицей ролей пользователей
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    user = relationship("User")
