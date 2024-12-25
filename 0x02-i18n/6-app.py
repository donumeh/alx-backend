#!/usr/bin/env python3


"""
Basic Flask App
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import List, Dict, Union

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

users: Dict[int, Dict[str, Union[str, None]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[None, Dict[str, Union[str, None]]]:
    """
    Get user from request or return None
    """
    user_id = request.args.get("login_as")
    if user_id:
        try:
            return users[int(user_id)]
        except (ValueError, KeyError):
            pass
    return None


@app.before_request
def before_request() -> None:
    """
    Set global user before each request
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Get locale from URL, user settings, request header, or default
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()