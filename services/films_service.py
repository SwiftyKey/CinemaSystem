from repository.films_repository import FilmsRepositorySQLAlchemy


class FilmService:  # сервис для общения с репозиторием фильмов
    films_repository = FilmsRepositorySQLAlchemy()

    def get_all(self):  # получить все фильмы
        return {"films": [item.to_dict(
                only=("id", "title", "release_date", "duration", "director", "genre_id"))
                for item in self.films_repository.get_all()]}

    def get_film(self, film_id):  # получить один фильм
        film = self.films_repository.get_film(film_id)
        if film:
            return {"film": [item.to_dict(
                    only=("id", "title", "release_date", "duration", "director", "genre_id"))
                    for item in [film]]}
        return {"error": "not found"}

    def add(self, film):  # добавить фильм
        self.films_repository.add(film)
        return {"success": "ok"}

    def update(self, film_id, film):  # изменить существующий фильм
        if self.films_repository.get_film(film_id):
            self.films_repository.update(film_id, film)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, film_id):  # удалить фильм
        if self.films_repository.get_film(film_id):
            self.films_repository.delete(film_id)
            return {"success": "ok"}
        return {"error": "not found"}
