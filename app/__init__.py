"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7ldjhp8u7g2edqb70-a.oregon-postgres.render.com",
        database="post_reg",
        user="post_reg_user",
        password="WYYsdsTLD6VxIibw9iIVGn9YiY95Y0L6")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
