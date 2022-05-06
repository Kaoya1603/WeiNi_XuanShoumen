from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired


class AddFavoriteForm(FlaskForm):
    competition = StringField('Название олимпиады', validators=[DataRequired()])
    profile = StringField('Профиль', validators=[DataRequired()])
    send_alerts_to_me = BooleanField('Отправлять уведомления о приближении олимпиады на почту')
    submit = SubmitField('Добавить')
