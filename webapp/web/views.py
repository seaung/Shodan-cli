from . import web
from webapp.web.forms import SearchForm


#@web.route('/search/', methods=['POST', 'GET'])
#def search():
#    form = SearchForm(request.form)
#    if request.method == 'POST':
#        if form.validate():
#            keyword = form.keywod.data
#
