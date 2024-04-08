from flask_restful import Resource

from services.roles_service import RolesService


class RoleResource(Resource):  # контроллер для работы с одной ролью
    roles_service = RolesService()

    def get(self, role_id):  # получить
        return self.roles_service.get_role(role_id)


class RoleListResources(Resource):  # контроллер для работы со списком записей
    roles_service = RolesService()

    def get(self):  # получить
        return self.roles_service.get_all()
