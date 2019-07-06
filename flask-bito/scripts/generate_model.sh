#!/usr/bin/env bash
flask-sqlacodegen mysql+pymysql://root@localhost:3306/bito_interview --flask > model.py
