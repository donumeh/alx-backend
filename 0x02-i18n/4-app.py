#!/usr/bin/env python3

"""
Basic Flask App
"""

from flask import Flask, request, render_template
from flask_babel import Babel
from typing import List

app: Flask = Flask(__name__)


class Config:
    """
    Config for Flask application
    """

    LANGUAGES: List = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)

babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get locale from request or default
    """
    locale: str = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
