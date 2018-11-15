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

    if request.method == "POST" and form.validate():
        keyword = form.keyword.data

        return redirect(url_for("host_lists"))
    return render_template("shodan.html", form=form)


@web.route("/hosts", methods=["GET"])
def host_lists():
    return render_template("result.html")
