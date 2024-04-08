from repository.genres_repository import GenresRepositorySQLAlchemy


class GenreService:  # сервис для общения с репозиторием жанров
    genres_repository = GenresRepositorySQLAlchemy()

    def all_genres(self):  # получить все жанры
        return {"genres": [item.to_dict(only=("title", "id"))
                           for item in self.genres_repository.get_all()]}

    def get_genre(self, genre_id):  # получить один жанр
        genre = self.genres_repository.get_genre(genre_id)
        if genre:
            return {"genres": [item.to_dict(only=("title", "id"))
                               for item in [genre]]}
