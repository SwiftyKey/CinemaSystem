from flask_login import logout_user


class LogoutUserService:  # сервис для выхода из аккаунта
    def logout_user(self):  # выход
        logout_user()
