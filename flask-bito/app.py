import os

from flask import Flask, Response, jsonify, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy

import pymysql

from model import db
from api import api

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('settings')

app.register_blueprint(api, url_prefix='/api')
db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
