from domain import db_session
from domain.session import Session
from datetime import datetime

db_session.global_init("../db/system.db")
session = db_session.create_session()

sessions = [Session(session_datetime=datetime(year=2021, month=4, day=20, hour=15), film_id=2),
            Session(session_datetime=datetime(year=2021, month=4, day=20, hour=18), film_id=8),
            Session(session_datetime=datetime(year=2021, month=4, day=21, hour=12), film_id=6),
            Session(session_datetime=datetime(year=2021, month=4, day=22, hour=15), film_id=5)]
session.add_all(sessions)
session.commit()
