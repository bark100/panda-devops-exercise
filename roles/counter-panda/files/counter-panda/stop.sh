#!/bin/bash
# stop the panda
kill -s SIGTERM $(pgrep -f counter)
