from flask import render_template


class MainController():
    def index():
        return render_template('main/index.html.jinja')