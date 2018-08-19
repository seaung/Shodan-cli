from flask import render_template
from . import web
from webapp.web.forms import SearchForm


#@web.route('/search/', methods=['POST', 'GET'])
#def search():
#    form = SearchForm(request.form)
#    if request.method == 'POST':
#        if form.validate():
#            keyword = form.keywod.data
#


#@web.route('/index')
#def index():
#    return render_template('index.html')
#
