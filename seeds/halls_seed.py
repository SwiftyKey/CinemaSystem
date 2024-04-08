from domain import db_session
from domain.hall import Hall

db_session.global_init("../db/system.db")
session = db_session.create_session()

halls = [Hall(title="1", cinema_id=1), Hall(title="2", cinema_id=1),
         Hall(title="1", cinema_id=2), Hall(title="2", cinema_id=2)]
session.add_all(halls)
session.commit()
