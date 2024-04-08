from repository.users_repository import UsersRepositorySQLAlchemy


class UserService:  # сервис для общения с репозиторием пользователей
    users_repository = UsersRepositorySQLAlchemy()

    def get_all(self):  # получить всех пользоватлей
        return {"users": [item.to_dict(only=("id", "login", "password", "email", "role_id"))
                          for item in self.users_repository.get_all()]}

    def get_user(self, user_id):  # получить пользователя
        user = self.users_repository.get_user(user_id)
        if user:
            return {"user": [item.to_dict(only=("id", "login", "password", "email", "role_id"))
                             for item in [user]]}
        return {"error": "not found"}

    def add(self, user):  # добавить пользователя
        self.users_repository.add(user)
        return {"success": "ok"}

    def update(self, user_id, new_user):  # изменить существующего пользователя
        if self.users_repository.get_user(user_id):
            self.users_repository.update(user_id, new_user)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, user_id):  # удалить пользователя
        if self.users_repository.get_user(user_id):
            self.users_repository.delete(user_id)
            return {"success": "ok"}
        return {"error": "not found"}
