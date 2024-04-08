from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class FilterTicketForm(FlaskForm):  # форма фильтрации билетов
    hall = SelectField("Залы", choices=[])
    date = SelectField("День", choices=[])
    submit = SubmitField('Показать')
