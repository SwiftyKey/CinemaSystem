from werkzeug.security import generate_password_hash

from domain import db_session
from domain.user import User

db_session.global_init("../db/system.db")
session = db_session.create_session()

users = [User(login="swifty", password=generate_password_hash("admin1"), role_id=1, email="slippery@gmail.com"),
         User(login="chaa54", password=generate_password_hash("admin2"), role_id=1, email="chaa54@mail.com")]
session.add_all(users)
session.commit()
