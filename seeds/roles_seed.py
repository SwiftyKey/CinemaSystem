from domain import db_session
from domain.role import Role

db_session.global_init("../db/system.db")
session = db_session.create_session()

roles = [Role(title="Админ"), Role(title="Пользователь")]
session.add_all(roles)
session.commit()
