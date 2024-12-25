#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List


app: Flask = Flask(__name__)


class Config:
    """
    Config for flask application
    """

    LANGUAGES: List = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)
babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get best match (lang) for user
    """

    return request.accept_languages.best_match(app.cofig["LANGUAGES"])


@app.route("/", strict_slashes=True)
def index() -> str:
    """
    Home Page
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()