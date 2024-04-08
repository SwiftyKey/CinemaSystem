from domain.hall import Hall
from domain.session import Session
from repository.halls_sessions_repository import HallsSessionsRepositorySQLAlchemy
from repository.halls_repository import HallsRepositorySQLAlchemy
from repository.sessions_repository import SessionsRepositorySQLAlchemy


class HallSessionService:  # сервис для общения с репозиторием залов-сессий
    halls_sessions_repository = HallsSessionsRepositorySQLAlchemy()
    hall_repository = HallsRepositorySQLAlchemy()
    session_repository = SessionsRepositorySQLAlchemy()

    def get_all(self):  # получить все залы-сессии
        halls_sessions = self.halls_sessions_repository.get_all()
        for i in range(len(halls_sessions)):
            halls_sessions[i] = (self.hall_repository.get_hall(halls_sessions[i][0]),
                                 self.session_repository.get_session(halls_sessions[i][1]))
        return {"halls_sessions": [{"hall_id": hall.id, "session_id": session.id}
                                   for hall, session in halls_sessions]}

    def get_hall_sessions(self, hall_id):  # получить зал-сессию
        hall_sessions = self.halls_sessions_repository.get_hall_sessions(hall_id)
        for i in range(len(hall_sessions)):
            hall_sessions[i] = (self.hall_repository.get_hall(hall_sessions[i][0])[0],
                                self.session_repository.get_session(hall_sessions[i][1])[0])
        return {"hall_session": [item.to_dict(only=("hall_id", "session_id"))
                                 for item in hall_sessions]}

    def add(self, hall: Hall, session: Session):  # добавить зал-сессию
        self.halls_sessions_repository.add(hall, session)
        return {'success': 'OK'}

    def update(self, hall: Hall, session: Session, new_session: Session):  # изменить зал-сессию
        self.halls_sessions_repository.update(hall, session, new_session)
        return {'success': 'OK'}

    def delete(self, hall: Hall, session: Session):  # удалить зал-сессию
        self.halls_sessions_repository.delete(hall, session)
        return {'success': 'OK'}
