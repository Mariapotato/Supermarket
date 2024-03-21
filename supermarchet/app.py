import json
from flask import Flask, render_template, request
from blueprint_query.route import blueprint_query

app = Flask(__name__)
with open('../db_config.json') as f:
    app.config['db_config'] = json.load(f)


app.register_blueprint(blueprint_query, url_prefix='/query')
# app.register_blueprint(blueprint_query_2, url_prefix='/query_2')
# app.register_blueprint(blueprint_query_3, url_prefix='/query_3')
@app.route('/')
def main_menu():
    return render_template('main_menu.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)