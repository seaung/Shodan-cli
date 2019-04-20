from flask import Blueprint


mshodan = Blueprint('mshodan', __name__)


from ShodanApp.blueprints.mshodan import *