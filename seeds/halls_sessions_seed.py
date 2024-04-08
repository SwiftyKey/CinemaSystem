from domain import db_session
from domain.hall_session import hall_session_table

db_session.global_init("../db/system.db")
session = db_session.create_session()

print((session.query(hall_session_table).all()))
