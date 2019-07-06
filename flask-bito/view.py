#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : view.py
# @Author  : dephin
# @File    : 2019-07-06
import os
import random

from flask import jsonify, request, Blueprint, abort

from model import PeopleInfo, PeopleSnapshot, db

ROOT_DIR = os.path.dirname(__file__)

api = Blueprint('api', __name__,
                static_folder=os.path.join(ROOT_DIR, 'dist', 'static'),
                template_folder=os.path.join(ROOT_DIR, 'dist')
                )


@api.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()


@api.route('/')
def hello_world():
    return 'Hello World!'


@api.route('/people-info', methods=['GET'])
def get_people_data():
    try:
        result = []
        for name in ('安装，实施人员', '工人', '销售', '项目开发', '其他'):
            data = []
            for i in range(0, 25):
                data.append(random.randint(1000, 2000))
            result.append({
                'name': name,
                'data': data
            })
        return jsonify(result)
    except:
        abort(500)


@api.route('/people-info/update', methods=['POST'])
def update_people_data():
    req_data = request.get_json()
    print(req_data)
    people_info = PeopleInfo(**req_data)
    db.session.add(people_info)
    db.session.commit()
    return jsonify(success=True)


@api.route('/people-snapshot', methods=['GET'])
def get_people_snapshot_data():
    limit = request.args.get('limit')
    records = PeopleSnapshot.query.limit(limit)
    resutl = {}
    for r in records:
        if r.name in resutl:
            resutl[r.name].append(r.data)
        else:
            resutl[r.name] = [r.data]
    ret = []
    for (k, v) in resutl.items():
        ret.append({
            'name': k,
            'data': v,
        })
    return jsonify(ret)


@api.route('/people-snapshot/update', methods=['POST'])
def update_people_snapshot_data():
    req_data = request.get_json()
    print(req_data)
    people_snapshot = PeopleSnapshot(**req_data)
    db.session.add(people_snapshot)
    return jsonify(success=True)


@api.errorhandler(500)
def server_error():
    return 'Server Error'
