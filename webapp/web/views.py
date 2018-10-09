from flask import render_template, request, flash
from . import web
from webapp.web.forms import SearchForm
from webapp.api.api import ShodanApi 


@web.route('/index')
def index():
    return render_template('shodan.html')


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)

    if request.method == "POST":
        if form.validate():
            keyword = form.keyword.data

            return render_template("result.html", data=data)

    return render_template("shodan.html", form=form)




