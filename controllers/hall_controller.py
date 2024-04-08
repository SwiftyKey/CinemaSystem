from flask_restful import Resource

from services.halls_service import HallService


class HallResource(Resource):  # контроллер для работы с одним холлом
    hall_service = HallService()

    def get(self, hall_id):  # получить
        return self.hall_service.get_hall(hall_id)

    def post(self, hall):  # добавить
        return self.hall_service.add(hall)

    def put(self, hall_id, hall):  # изменить
        return self.hall_service.update(hall_id, hall)

    def delete(self, hall_id):  # удалить
        return self.hall_service.delete(hall_id)


class HallListResources(Resource):  # контроллер для работы со списком ресурсов
    hall_service = HallService()

    def get(self):  # получить
        return self.hall_service.get_all()
