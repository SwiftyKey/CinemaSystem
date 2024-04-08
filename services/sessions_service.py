from repository.sessions_repository import SessionsRepositorySQLAlchemy


class SessionService:  # сервис для общения с репозиторием сессий
    sessions_repository = SessionsRepositorySQLAlchemy()

    def get_all(self):  # получить все сессии
        return {"sessions": [item.to_dict(only=("id", "session_datetime", "film_id"))
                             for item in self.sessions_repository.get_all()]}

    def get_session(self, session_id):  # получить сессию
        session = self.sessions_repository.get_session(session_id)
        if session:
            return {"session": [item.to_dict(only=("id", "session_datetime", "film_id"))
                                for item in [session]]}
        return {"error": "not found"}

    def add(self, session):  # добавить сессию
        self.sessions_repository.add(session)
        return {"success": "ok"}

    def update(self, session_id, session):  # изменить существующую сессию
        if self.sessions_repository.get_session(session_id):
            self.sessions_repository.update(session_id, session)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, session_id):  # удалить сессию
        if self.sessions_repository.get_session(session_id):
            self.sessions_repository.delete(session_id)
            return {"success": "ok"}
        return {"error": "not found"}
