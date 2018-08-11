from flask import Blueprint

web = Blueprint('web', __name__)

from webapp.web.views import *
from webapp.web.forms import *

