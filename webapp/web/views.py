from flask import render_template, request
from . import web
from webapp.web.forms import SearchForm


@web.route('/index')
def index():
    return render_template('index.html')


#@web.route('/index', methods=['GET', 'POST'])
#def search():
#    form = SearchForm(request.data)
#
#    if request.method == 'GET':
#        pass
#    elif request.method == 'POST':
#        pass
#    return render('search.html')
