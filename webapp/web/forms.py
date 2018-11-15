#from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField
from wtforms.validators import Length, DataRequired

from webapp.utils.ip import is_ip


class SearchForm(Form):
    keyword = StringField(validators=[Length(min=6, max=120), DataRequired()])

    def validate_keyword(self, value):
        if is_ip(value):
            pass
        elif value:
            pass
        else:
            pass
