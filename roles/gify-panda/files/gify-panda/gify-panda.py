#!/usr/bin/env python

import os,sys
from random import choice
from flask import url_for, render_template, Flask

pid = str(os.getpid())
pidfile = "/tmp/gify-panda.pid"

panda_roulette = Flask(__name__)

@panda_roulette.route("/roll_panda")
def random_panda():
    names = os.listdir(os.path.join(panda_roulette.static_folder, 'resources'))
    img_url = url_for('static', filename=os.path.join('resources', choice(names)))
    return render_template('random_image.html', img_url=img_url)

if __name__ == "__main__":
  if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()

  file(pidfile, 'w').write(pid)
  try:
    panda_roulette.run(host='0.0.0.0')
  finally:
    os.unlink(pidfile)
