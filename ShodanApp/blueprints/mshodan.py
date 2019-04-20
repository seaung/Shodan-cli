import re
import socket

from flask import render_template, request, flash
from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired

from . import mshodan
from ShodanApp.shodans import MShodan


mshdan = MShodan()


class SearchForm(Form):
    keyword = StringField(validators=[DataRequired()])


def converter_address(address):
    try:
        addr = socket.gethostbyname(address)
        return True, addr
    except socket.gaierror as e:
        print(f'{e}')
        return False, address


def is_a_host(keyword):
    pattern = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')

    ok, address = converter_address(keyword)

    result = True if ok and pattern.findall(address) else False
    return result


@mshodan.route('/shodan_index', methods=['GET', ])
def shodan():
    return render_template('shodans/mshodans.html')


@mshodan.route('/search', methods=['GET', 'POST'])
def msearch():
    form = SearchForm(request.form)
    print(form.keyword.data)
    results = None
    if form.validate():
        keyword = form.keyword.data.strip()
        if is_a_host(keyword):
            results = mshdan.look_up_a_host(keyword)
        else:
            results = mshdan.searching_shodan(keyword)
    else:
        flash("搜索关键词有问题!")

    return render_template('shodans/results.html', data=results)
