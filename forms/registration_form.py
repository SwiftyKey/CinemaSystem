from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):  # форма регистрации
    email = EmailField(validators=[DataRequired()])
    login = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_again = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')
