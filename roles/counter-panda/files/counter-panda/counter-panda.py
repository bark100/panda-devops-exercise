#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
import os,sys

pid = str(os.getpid())
pidfile = "/tmp/counter-panda.pid"

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
  if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()

  file(pidfile, 'w').write(pid)
  try:
    app.run(host='0.0.0.0', port=5001)
  finally:
    os.unlink(pidfile)
