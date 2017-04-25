#!/bin/bash
( ( nohup python /tmp/counter-panda/counter-panda.py 1>/dev/null 2>&1 ) & )
