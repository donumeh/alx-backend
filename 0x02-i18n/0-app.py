#!/usr/bin/env python3

"""
Basic Flask app
"""

from flask import Flask, render_template


app: Flask = Flask(__name__)


@app.route('/', strict_slashes=True)
def index() -> str:
    """
    Home Page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
