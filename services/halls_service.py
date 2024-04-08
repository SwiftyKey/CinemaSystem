from repository.halls_repository import HallsRepositorySQLAlchemy


class HallService:  # сервис для общения с репозиторием холлов
    halls_repository = HallsRepositorySQLAlchemy()

    def get_all(self):  # получить все холлы
        return {"halls": [item.to_dict(only=("id", "title", "cinema_id"))
                          for item in self.halls_repository.get_all()]}

    def get_hall(self, hall_id):  # получить один холл
        hall = self.halls_repository.get_hall(hall_id)
        if hall:
            return {"hall": [item.to_dict(only=("id", "title", "cinema_id"))
                             for item in [hall]]}
        return {"success": "ok"}

    def add(self, hall):  # добавить холл
        self.halls_repository.add(hall)
        return {"success": "ok"}

    def update(self, hall_id, hall):  # изменить существующий холл
        if self.halls_repository.get_hall(hall_id):
            self.halls_repository.update(hall_id, hall)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, hall_id):  # удалить холл
        if self.halls_repository.get_hall(hall_id):
            self.halls_repository.delete(hall_id)
            return {"success": "ok"}
        return {"error": "not found"}
