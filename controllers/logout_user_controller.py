from services.logout_user_service import LogoutUserService


class LogoutUser:  # контроллер для работы с функционалом выхода пользователя из аккаунта
    logout_user_service = LogoutUserService()

    def logout(self):  # выйти
        return self.logout_user_service.logout_user()
