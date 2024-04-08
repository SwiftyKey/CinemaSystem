from flask_restful import Resource

from services.cinemas_service import CinemasService


class CinemasResource(Resource):  # контроллер для работы с одним кинотеатром
    cinemas_service = CinemasService()

    def get(self, cinema_id):  # получить
        return self.cinemas_service.get_cinema(cinema_id)

    def post(self, cinema):  # добавить
        return self.cinemas_service.add(cinema)

    def put(self, cinema_id, cinema):  # изменить
        return self.cinemas_service.update(cinema_id, cinema)

    def delete(self, cinema_id):  # удалить
        return self.cinemas_service.delete(cinema_id)


class CinemasListResources(Resource):  # контроллер для работы со списком кинотеатров
    cinemas_service = CinemasService()

    def get(self):  # получить
        return self.cinemas_service.get_all()
