from flask_restful import Resource

from services.genre_service import GenreService


class GenreResources(Resource):  # контроллер для работы с одним жанром
    genre_service = GenreService()

    def get(self, genre_id):  # получить
        return self.genre_service.get_genre(genre_id)


class GenreListResources(Resource):  # контроллер для работы со списком жанров
    genre_service = GenreService()

    def get(self):  # получить
        return self.genre_service.all_genres()
