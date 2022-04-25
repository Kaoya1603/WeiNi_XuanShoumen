from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    competition = StringField('Название олимпиады', validators=[DataRequired()])
    profile = SelectField('Профиль', choices=[], validators=[DataRequired()])
    submit = SubmitField('Поиск')
