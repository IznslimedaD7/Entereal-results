from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class AuthForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=6, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=5, max=60)])
    submit = SubmitField('Войти')