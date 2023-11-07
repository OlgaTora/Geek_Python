import os

from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path="/static")


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/{page}")
def get_base_page():
    return index()


@app.route("/shop/{page}")
def get_page(page: str):
    if os.path.exists(f'templates/{page}.html'):
        return app.send_static_file(f'templates/{page}.html')
    else:
        return app.send_static_file(f'templates/404.html')
