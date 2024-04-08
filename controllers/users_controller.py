from flask_restful import Resource
from services.user_service import UserService


class UserResource(Resource):  # контроллер для работы с одним пользователем
    user_service = UserService()

    def get(self, user_id):  # получить
        return self.user_service.get_user(user_id)

    def post(self, user):  # добавить
        return self.user_service.add(user)

    def put(self, user_id, new_user):  # изменить
        return self.user_service.update(user_id=user_id, new_user=new_user)

    def delete(self, user_id):  # удалить
        return self.user_service.delete(user_id)


class UsersListResources(Resource):  # контроллер для работы со списком пользователей
    user_service = UserService()

    def get(self):  # получить
        return self.user_service.get_all()
