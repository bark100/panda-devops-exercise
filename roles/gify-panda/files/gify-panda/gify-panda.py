#!/usr/bin/env python

import os
from random import choice
from flask import url_for, render_template, Flask


panda_roulette = Flask(__name__)

@panda_roulette.route("/roll_panda")
def random_panda():
    names = os.listdir(os.path.join(panda_roulette.static_folder, 'resources'))
    img_url = url_for('static', filename=os.path.join('resources', choice(names)))

    return render_template('random_image.html', img_url=img_url)

if __name__ == "__main__":
    panda_roulette.run()