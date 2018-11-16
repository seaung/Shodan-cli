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

    matchers = MatchersCollection()

    if request.method == "POST" and form.validate():
        keyword = form.keyword.data.strip()
        
        ip_or_keyword = is_ip_or_keyword(keyword)

        if ip_or_keyword == 'ip_address':
            search_collection = SearchCollection()
            search_collection.search_by_ip(keyword)
        else:
            search_collection = SearchCollection()
            search_collection.search_by_host(keyword)
        matchers.fill(search_collection, keyword)
        return render_template("result.html", data=matchers)
    else:
        flash("errors.")

    return render_template("shodan.html", form=form)


@web.route("/hosts", methods=["GET"])
def host_lists():
    return render_template("result.html")

