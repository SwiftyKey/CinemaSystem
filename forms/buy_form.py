from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BuyForm(FlaskForm):  # форма для покупки
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    number_card = StringField(validators=[DataRequired()])
    code_security = StringField(validators=[DataRequired()])
    submit = SubmitField('Оплатить')
