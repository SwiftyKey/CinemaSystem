from domain.user import User
from controllers.users_controller import UserResource, UsersListResources
from forms.registration_form import RegistrationForm
from werkzeug.security import generate_password_hash


class RegistrationService:  # сервис для регистрации пользователя
    user_resource = UserResource()
    user_list_resource = UsersListResources()

    def registration(self, form: RegistrationForm):  # регистрация
        user = User()
        user.login = form.login.data
        user.email = form.email.data
        user.password = form.password.data
        user.role_id = 2
        repeat_password = form.password_again.data
        if user.password == repeat_password:
            user.password = generate_password_hash(user.password)
            try:
                self.user_resource.post(user)
                return ""
            except Exception:
                return "Такой пользователь уже есть в базе данных"
        else:
            return "Пароли не совпадают"
