from flask import Blueprint, render_template, request, current_app
from work_with_db import select_dict
import os
from sql_provider import SQLProvider


blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_query.route('/menu', methods=['GET', 'POST'])
def main_menu():
    return render_template('index.html')

@blueprint_query.route('/second_menu', methods=['GET', 'POST'])
def second_menu():
    _sql = provider.get('all.sql')
    products = select_dict(current_app.config['db_config'], _sql)
    return render_template('dynamic.html', products=products)

@blueprint_query.route('/1', methods=['GET', 'POST'])
def query_index_1():
    if request.method == 'GET':
        return render_template('input_param.html')
    else:
        category = request.form.get('category')
        #price = request.form.get('price')
        #_sql = provider.get('product_1.sql', category=category, price=price)
        _sql = provider.get('product_1.sql', category=category)
        products = select_dict(current_app.config['db_config'], _sql)

        if products:
            prod_title = 'Результат поиска продуктов, которые стоят дороже указанной цены'
            return render_template('dynamic.html', products=products, prod_title=prod_title)
        else:
            return render_template('no_result.html')

@blueprint_query.route('/2', methods=['GET', 'POST'])
def query_index_2():
    if request.method == 'GET':
        return render_template('input_param2.html')
    else:
        #category = request.form.get('category')
        price = request.form.get('price')
        _sql = provider.get('product_2.sql', price=price)
        products = select_dict(current_app.config['db_config'], _sql)

        if products:
            prod_title = 'Результат поиска продуктов, которые стоят дешевле указанной цены'
            return render_template('dynamic.html', products=products, prod_title=prod_title)
        else:
            return render_template('no_result.html')

@blueprint_query.route('/3', methods=['GET', 'POST'])
def query_index_3():
    if request.method == 'GET':
        return render_template('input_param3.html')
    else:
        category = request.form.get('category')
        price = request.form.get('price')
        _sql = provider.get('product_3.sql', category=category, price=price, prod_price=price)
        products = select_dict(current_app.config['db_config'], _sql)

        if products:
            prod_title = 'Результат поиска продуктов, которое можно купить за указанные суммы'
            return render_template('dynamic_3.html', products=products, price = int(price), prod_title=prod_title)
        else:
            return render_template('no_result.html')
