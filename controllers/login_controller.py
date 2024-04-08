from forms.authorisation_form import AuthorisationForm
from services.login_service import LoginService


class LoginResource:  # контроллер для работы с функционалом авторизации пользователя
    login_service = LoginService()

    def login(self, form: AuthorisationForm):  # авторизация
        return self.login_service.login(form)
