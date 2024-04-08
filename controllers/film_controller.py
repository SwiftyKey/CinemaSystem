from flask_restful import Resource

from services.films_service import FilmService


class FilmResource(Resource):  # контроллер для работы с одним фильмом
    film_service = FilmService()

    def get(self, film_id):  # получить
        return self.film_service.get_film(film_id)

    def post(self, film):  # добавить
        return self.film_service.add(film)

    def put(self, film_id, film):  # изменить
        return self.film_service.update(film_id, film)

    def delete(self, film_id):  # удалить
        return self.film_service.delete(film_id)


class FilmListResources(Resource):  # контроллер для работы со списокм фильмов
    film_service = FilmService()

    def get(self):  # получить
        return self.film_service.get_all()
