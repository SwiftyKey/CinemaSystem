from flask_restful import Resource

from services.chairs_service import ChairService


class ChairResource(Resource):  # контроллер для работы с одним креслом
    chair_service = ChairService()

    def get(self, chair_id):  # получить
        return self.chair_service.get_chair(chair_id)

    def post(self, chair):  # добавить
        return self.chair_service.add(chair)

    def put(self, chair_id, chair):  # изменить
        return self.chair_service.update(chair_id, chair)

    def delete(self, chair_id):  # удалить
        return self.chair_service.delete(chair_id)


class ChairListResources(Resource):  # контроллер для работы со списком кресел
    chair_service = ChairService()

    def get(self):  # получить
        return self.chair_service.get_all()
