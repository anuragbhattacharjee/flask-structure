import config
import json
import logging
import os

from flask import Flask, jsonify
from flask_restful import Resource, Api
from bs4 import BeautifulSoup

from app.resources.welcome import Welcome


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                        os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()

app = Flask(__name__)
api = Api(app)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevConfig")

logger.info(f'Starting app in {app.config["ENV"]} environment')

api.add_resource(Welcome, '/', '/hello')
