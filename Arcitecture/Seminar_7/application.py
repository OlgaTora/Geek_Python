import os

from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<string:page>/')
def get_page():
    return index()


@app.route('/get-page-html/<string:page>/')
def get_page_html(page: str):
    if os.path.exists(f'templates/{page}.html'):
        return render_template(f'{page}.html')
    else:
        return app.send_static_file('404.html')
