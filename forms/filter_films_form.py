from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class FilterFilmForm(FlaskForm):  # форма фильтрации фильмов
    genre = SelectField("Жанры", choices=[])
    cinema = SelectField("Кинотеатры", choices=[])
    submit = SubmitField('Показать')
