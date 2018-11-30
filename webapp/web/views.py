from flask import render_template, request, flash
from . import web
from webapp.web.forms import SearchForm
from webapp.api.api import ShodanApi
from webapp.utils.ip import is_ip


@web.route('/index')
def index():
    return render_template('shodan.html')


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)

    if form.validate():
        keyword = form.keyword.data.strip()
        if is_ip(keyword):
            results = ShodanApi.search_by_ip(keyword)
        else:
            results = ShodanApi.search_by_host(keyword)

    return render_template('result'.html', form=form, data=results)
