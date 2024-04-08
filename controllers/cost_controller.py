from flask_restful import Resource

from services.cost_service import CostService


class CostResource(Resource):  # контроллер для работы с одной ценой
    cost_service = CostService()

    def get(self, cost_id):  # получить
        return self.cost_service.get_cost(cost_id)

    def post(self, cost):  # добавить
        return self.cost_service.add(cost)

    def put(self, cost_id, cost):  # изменить
        return self.cost_service.update(cost_id, cost)

    def delete(self, cost_id):  # удалить
        return self.cost_service.delete(cost_id)


class CostListResources(Resource):  # контроллер для работы со списком цен
    cost_service = CostService()

    def get(self):  # получить
        return self.cost_service.get_all()
