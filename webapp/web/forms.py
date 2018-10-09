#from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField
from wtforms.validators import Length, DataRequired


class SearchForm(Form):
    keyword = StringField(validators=[Length(min=6, max=120), DataRequired()])

    def validate_keyword(self, value):
        pass


