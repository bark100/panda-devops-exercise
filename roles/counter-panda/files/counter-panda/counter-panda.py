#!/usr/bin/env python

from flask import Flask, request # use Flask micro framework for running the service
from flask_restful import Resource, Api # easy restful resource declarations
import os,sys

pid = str(os.getpid()) # get PID number of current interpreter
pidfile = "/tmp/counter-panda.pid"

app = Flask(__name__) # declare new Flask app
api = Api(app) # declare new Api instance

counter = 0 # reset panda counter

class count(Resource): # declare new class of type counter

    def post(self): # define function for http posting
        global counter # declare global counter variable to be shared amongst functions
        counter = counter + 1 # increase counter by 1 on each http post
        return 'I <3 Python'

    def get(self): 
        return {"Number of pandas: ": counter} # return number of http posts

# return error on bad uri by using throw-away temporary function
app.register_error_handler(404, lambda e: '\nBad panda. Please use \'/\' as endpoint.\n\n')
# map counter class to uri
api.add_resource(count, '/')

if __name__ == '__main__': # execute code only if script is run directly
  if os.path.isfile(pidfile): # make sure script is not running 
    print "%s already exists, exiting" % pidfile
    sys.exit()

  file(pidfile, 'w').write(pid) # write PID to file
  try: # start a new Flask server
    app.run(host='0.0.0.0', port=5001)
  finally: # remove PID file upon shutdown
    os.unlink(pidfile)
