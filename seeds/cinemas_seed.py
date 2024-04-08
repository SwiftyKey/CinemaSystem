from domain import db_session
from domain.cinema import Cinema

db_session.global_init("../db/system.db")
session = db_session.create_session()

cinemas = [Cinema(title="Кинотеатр №1"), Cinema(title="Кинотеатр №2")]
session.add_all(cinemas)
session.commit()
