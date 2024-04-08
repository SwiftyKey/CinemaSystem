from domain import db_session
from domain.chair import Chair

db_session.global_init("../db/system.db")
session = db_session.create_session()

hall_ids = [1, 2, 3, 4]
chairs = [Chair(row=i, place=j, hall_id=hall_id) for hall_id in hall_ids for i in range(1, 11) for j in range(1, 15)]

session.add_all(chairs)
session.commit()
