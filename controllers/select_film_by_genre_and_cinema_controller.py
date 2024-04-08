from flask_restful import Resource
from services.select_film_by_genre_and_cinema_service import SelectFilmService


class SelectFilmResource(Resource):  # контроллер для работы с фукнционалом выбора фильмов
    select_film_service = SelectFilmService()

    def get(self, cinema_id, genre_id):  # получить
        return self.select_film_service.select_film(cinema_id, genre_id)
