from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NominationForm(FlaskForm):
    title = StringField('Название номинации', validators=[DataRequired(), Length(min=6, max=150)])
    description = StringField('Описание номинации(необязательно)')
    submit = SubmitField('Предложить')

class NominatForm(FlaskForm):
    title = StringField('Номинат', validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField('Номинировать')