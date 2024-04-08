from repository.costs_repository import CostsRepositorySQLAlchemy


class CostService:  # сервис для общения с репозиторием цен
    cost_repository = CostsRepositorySQLAlchemy()

    def get_all(self):  # получить все цены
        return {"costs": [item.to_dict(only=("id", "cost", "session_id"))
                          for item in self.cost_repository.get_all()]}

    def get_cost(self, cost_id):  # получить одну цену
        cost = self.cost_repository.get_cost(cost_id)
        if cost:
            return {"cost": [item.to_dict(only=("id", "cost", "session_id"))
                             for item in [cost]]}

    def add(self, cost):  # добавить цену
        self.cost_repository.add(cost)
        return {"success": "ok"}

    def update(self, cost_id, cost):  # изменить существующую цену
        if self.cost_repository.get_cost(cost_id):
            self.cost_repository.update(cost_id, cost)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, cost_id):  # удалить цену
        if self.cost_repository.get_cost(cost_id):
            self.cost_repository.delete(cost_id)
            return {"success": "ok"}
        return {"error": "not found"}
