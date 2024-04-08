from controllers.film_controller import FilmListResources, FilmResource
from controllers.hall_controller import HallListResources
from controllers.hall_session_controller import HallSessionListResources
from controllers.session_controller import SessionListResources, SessionResource


class SelectFilmService:  # сервис для фильтрации фильмов по кинотеатру и жанру
    hall_resource = HallListResources()
    films_resource = FilmListResources()
    film_resource = FilmResource()
    hall_session_resource = HallSessionListResources()
    sessions_resource = SessionListResources()
    session_resource = SessionResource()

    def select_film(self, cinema_id, genre_id):  # отфильтровать фильмы
        all_halls = self.hall_resource.get()["halls"]
        all_films = self.films_resource.get()["films"]
        all_sessions = self.sessions_resource.get()["sessions"]
        halls_sessions = self.hall_session_resource.get()["halls_sessions"]
        halls = []
        films = []
        sessions = []
        necessary_films = []

        for hall in all_halls:
            if hall["cinema_id"] == cinema_id:
                halls.append(hall["id"])

        for film in all_films:
            if film["genre_id"] == genre_id:
                films.append(film["id"])

        for session in all_sessions:
            if session["film_id"] in films:
                sessions.append(session["id"])

        for hall_session in halls_sessions:
            for hall_id in halls:
                if hall_session["hall_id"] == hall_id:
                    for session_id in sessions:
                        if hall_session["session_id"] == session_id:
                            session = self.session_resource.get(session_id)["session"][0]
                            film = self.film_resource.get(session["film_id"])["film"][0]
                            if film["id"] not in [i["id"] for i in necessary_films]:
                                film.setdefault("halls_id", "")
                                film.setdefault("sessions_id", "")
                                film["sessions_id"] += f"{session_id}"
                                film["halls_id"] += f"{hall_id}"
                                necessary_films.append(film)
                            else:
                                film = list(filter(lambda x: x["id"] == "film_id",
                                                   necessary_films))[0]
                                index = necessary_films.index(film)
                                necessary_films[index]["sessions_id"] += f",{session_id}"
                                necessary_films[index]["halls_id"] += f",{hall_id}"

        return {"films": necessary_films}
