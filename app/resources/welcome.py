from flask import render_template, make_response
from flask_restful import Resource

class Welcome(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html', 'Etag': 'some-opaque-string'}
        return make_response(render_template('home.html'), 201, headers)