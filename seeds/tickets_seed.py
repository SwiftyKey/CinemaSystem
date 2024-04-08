from domain import db_session
from domain.ticket import Ticket

db_session.global_init("../db/system.db")
new_session = db_session.create_session()

tickets = []
chairs = [9, 10, 19, 20, 47,
          152, 153, 178, 183, 184,
          297, 298, 318, 319, 328,
          438, 450, 455, 456, 460]
sessions = [1, 3, 4, 2]
numbers = [1111, 1112, 1113, 1114, 1116,
           1115, 1118, 1119, 1122, 1125,
           1135, 1137, 1139, 1140, 1143,
           1149, 1152, 1153, 1156, 1159]
for session_index in range(len(sessions)):
    for chair, number in zip(chairs[session_index * 5: session_index * 5 + 5],
                             numbers[session_index * 5: session_index * 5 + 5]):
        tickets.append(Ticket(number=number, session_id=sessions[session_index],
                              chair_id=chair, cost=int(0.3 * number)))

new_session.add_all(tickets)
new_session.commit()