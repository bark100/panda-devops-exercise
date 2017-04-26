#!/bin/bash
# send python interpreter to background without creating nohup garbage
( ( nohup python /tmp/counter-panda/counter-panda.py 1>/dev/null 2>&1 ) & )
