#!/usr/bin/env python

import os,sys # use core operating system helper functions
from random import choice # random functions
from flask import url_for, render_template, Flask

pid = str(os.getpid()) # get current interpreter PID number
pidfile = "/tmp/gify-panda.pid"

panda_roulette = Flask(__name__) # declare new Flask app

@panda_roulette.route("/roll_panda")  # map random_panda function to root uri
def random_panda(): # how we randomize pandas
    names = os.listdir(os.path.join(panda_roulette.static_folder, 'resources')) # get panda names from resource folder
    img_url = url_for('static', filename=os.path.join('resources', choice(names))) # generate panda urls from static folder + random panda
    return render_template('random_image.html', img_url=img_url) # show panda, passing panda url to html template

if __name__ == "__main__": # execute only when running script directly
  if os.path.isfile(pidfile): # make sure script is not already run
    print "%s already exists, exiting" % pidfile
    sys.exit()

  file(pidfile, 'w').write(pid)
  try:
    panda_roulette.run(host='0.0.0.0') # run Flask server
  finally:
    os.unlink(pidfile)
