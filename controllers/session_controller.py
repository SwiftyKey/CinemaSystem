from flask_restful import Resource

from services.sessions_service import SessionService


class SessionResource(Resource):  # контроллер для работы с одной сессией
    session_service = SessionService()

    def get(self, session_id):  # поллучить
        return self.session_service.get_session(session_id)

    def post(self, session):  # добавить
        return self.session_service.add(session)

    def put(self, session_id, session):  # изменить
        return self.session_service.update(session_id, session)

    def delete(self, session_id):  # удалить
        return self.session_service.delete(session_id)


class SessionListResources(Resource):  # контроллер для работы со списком сессий
    session_service = SessionService()

    def get(self):  # получить
        return self.session_service.get_all()
