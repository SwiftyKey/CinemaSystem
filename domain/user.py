from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, SerializerMixin, UserMixin):  # модель для работы с таблицей пользователей
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    record = relationship("Record")

    role_id = Column("role_id", Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("Role", back_populates="user")
