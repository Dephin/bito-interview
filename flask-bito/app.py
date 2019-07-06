import os

from flask import Flask, Response, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

import pymysql

from model import db
from view import api

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('settings')

app.register_blueprint(api, url_prefix='/api')
db.init_app(app)

if __name__ == '__main__':
    app.run()
