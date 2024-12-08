from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=6, max=50)])
    nickname = StringField('Никнейм', validators=[DataRequired(), Length(min=5, max=80)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=5, max=60)])
    submit = SubmitField('Войти')

