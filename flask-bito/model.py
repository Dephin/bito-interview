# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class PeopleInfo(db.Model):
    __tablename__ = 'people_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())


class PeopleSnapshot(db.Model):
    __tablename__ = 'people_snapshot'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    data = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
