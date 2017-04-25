#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

counter = 0

class count(Resource):

    def post(self):
        global counter
        counter = counter + 1
        return 'I <3 Python'

    def get(self):
        return {"Number of pandas: ": counter}

app.register_error_handler(404, lambda e: '\nBad panda. Please use \'/\' as endpoint.\n\n')
api.add_resource(count, '/')

if __name__ == '__main__':
    app.run(debug=False)