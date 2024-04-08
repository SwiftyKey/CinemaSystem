from flask_restful import Resource

from services.registration_service import RegistrationService


class RegistrationResource(Resource):  # контроллер для работы с функционалом регистрации
    registration_service = RegistrationService()

    def registration(self, form):  # зарегестрироваться
        return self.registration_service.registration(form)
