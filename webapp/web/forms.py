from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired


class SearchForm(FlaskForm):
    keyword = StringField(validators=[Length(min=6, max=120), DataRequired()])

