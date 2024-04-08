import os

from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required

from api import blueprint
from controllers.book_controller import BookResource
from controllers.buy_controller import BuyResource
from controllers.cinemas_controller import CinemasListResources
from controllers.genre_controller import GenreListResources
from controllers.hall_controller import HallResource
from controllers.login_controller import LoginResource
from controllers.logout_user_controller import LogoutUser
from controllers.personal_area_controller import PersonalAreaResource
from controllers.registration_controller import RegistrationResource
from controllers.select_film_by_genre_and_cinema_controller import SelectFilmResource
from controllers.select_ticket_controller import SelectTicketResource
from controllers.session_controller import SessionResource
from domain import db_session
from domain.user import User
from forms.authorisation_form import AuthorisationForm
from forms.buy_form import BuyForm
from forms.filter_films_form import FilterFilmForm
from forms.filter_tickets_form import FilterTicketForm
from forms.registration_form import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandex_lyceum_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)

filter_ticket_form = None
url_tickets = ""


def filter_film_form_data():  # добавление данных для формы фильтрации фильмов
    cinemas_resource = CinemasListResources()
    cinemas = cinemas_resource.get()["cinemas"]
    genres_resources = GenreListResources()
    genres = genres_resources.get()["genres"]
    filter_film_form = FilterFilmForm()
    filter_film_form.genre.choices = [(genre["id"], genre["title"]) for genre in genres]
    filter_film_form.cinema.choices = [(cinema["id"], cinema["title"]) for cinema in cinemas]
    return filter_film_form


# добавление данных для формы фильтрации билетов
def filter_ticket_form_data(halls: str, sessions: str):
    halls_resource = HallResource()
    halls = [halls_resource.get(int(hall_id))["hall"][0] for hall_id in halls.split(",")]
    sessions_resource = SessionResource()
    sessions = sorted([sessions_resource.get(int(session_id))["session"][0]
                       for session_id in sessions.split(",")], key=lambda x: x["session_datetime"])
    filter_ticket_form = FilterTicketForm()
    filter_ticket_form.hall.choices = [(hall["id"], hall["title"]) for hall in halls]
    filter_ticket_form.date.choices = [(session["id"], session["session_datetime"])
                                       for session in sessions]
    return filter_ticket_form


@login_manager.user_loader
def load_user(user_id):  # получение пользователя из бд
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/", methods=["GET", "POST"])
def index():  # фукнция для основной страницы и фильтрации фильмов
    filter_film_form = filter_film_form_data()
    if filter_film_form.validate_on_submit():
        return redirect(
            f"/filter_by/{int(filter_film_form.cinema.data)},{int(filter_film_form.genre.data)}")
    return render_template("index.html", name_page="Основная", filter_film_form=filter_film_form)


@app.route("/filter_by/<int:cinema>,<int:genre>", methods=["GET", "POST"])
def filter_films(cinema, genre):  # функция для страницы показа фильмов
    filter_film_form = filter_film_form_data()
    resource = SelectFilmResource()
    films = resource.get(cinema, genre)["films"]
    if filter_film_form.validate_on_submit():
        return redirect(
            f"/filter_by/{int(filter_film_form.cinema.data)},{int(filter_film_form.genre.data)}")
    return render_template("index.html", name_page="Фильмы",
                           filter_film_form=filter_film_form, films=films)


@app.route("/tickets_index/<string:halls>,<string:sessions>", methods=["GET", "POST"])
def tickets_index(halls, sessions):  # функция для страницы фильтрации билетов
    global filter_ticket_form, url_tickets
    filter_ticket_form = filter_ticket_form_data(halls, sessions)
    if filter_ticket_form.validate_on_submit():
        hall, date = int(filter_ticket_form.hall.data), int(filter_ticket_form.date.data)
        url_tickets = f"/filter_tickets/{hall},{date}"
        return redirect(url_tickets)
    return render_template("index.html", name_page="Билеты",
                           filter_ticket_form=filter_ticket_form)


@app.route("/filter_tickets/<int:hall>,<int:session>", methods=["GET", "POST"])
def filter_tickets(hall, session):  # функция для страницы показа билетов
    global filter_ticket_form, url_tickets
    resource = SelectTicketResource()
    tickets = resource.get(hall, session)["tickets"]
    if filter_ticket_form.validate_on_submit():
        hall, date = int(filter_ticket_form.hall.data), int(filter_ticket_form.date.data)
        url_tickets = f"/filter_tickets/{hall},{date}"
        return redirect(url_tickets)
    return render_template("index.html", name_page="Билеты",
                           filter_ticket_form=filter_ticket_form, tickets=tickets)


@app.route("/buy/<int:ticket>", methods=["GET", "POST"])
def buy(ticket):  # функция для покупки билетов
    form = BuyForm()
    if form.validate_on_submit():
        resource = BuyResource()
        resource.buy(ticket)
        return redirect(url_tickets)
    return render_template("index.html", name_page="Покупка", buy_form=form)


@app.route("/book/<int:ticket>", methods=["GET", "POST"])
def book(ticket):  # функция для бронирования билетов
    resource = BookResource()
    resource.book(ticket)
    return redirect(url_tickets)


@app.route("/personal_area", methods=["GET", "POST"])
def personal_area():  # функция для страницы показа личного кабинета
    resource = PersonalAreaResource()
    tickets = resource.get_user_tickets()
    return render_template("index.html", name_page="Кабинет", user_tickets=tickets)


@app.route("/authorisation", methods=["GET", "POST"])
def authorisation():  # функция для страницы авторизации
    form = AuthorisationForm()
    if form.validate_on_submit():
        resource = LoginResource()
        message = resource.login(form)
        if message:
            return render_template("authorisation.html", name_page="Авторизация",
                                   type_page="Авторизация", message=message, form=form)
        else:
            return redirect("/")
    return render_template("authorisation.html", type_page="Авторизация",
                           name_page="Авторизация", form=form)


@app.route("/registration", methods=["GET", "POST"])
def registration():  # функция для страницы регистрации
    form = RegistrationForm()
    if form.validate_on_submit():
        resource = RegistrationResource()
        message = resource.registration(form)
        if message:
            return render_template("registration.html", name_page="Регистрация",
                                   type_page="Регистрация", message=message, form=form)
        else:
            return redirect("/")
    return render_template("registration.html", type_page="Регистрация",
                           name_page="Регистрация", form=form)


@app.route("/logout")
@login_required
def logout():  # функция для выхода из аккаунта пользователя
    resource = LogoutUser()
    resource.logout()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init("./db/system.db")
    app.register_blueprint(blueprint)
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host="0.0.0.0")
