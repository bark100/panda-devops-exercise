#!/usr/bin/env python

import argparse
import subprocess # we use subprocess to saftely execute ansible

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Panda services deployer tool version 0.1')
    parser.add_argument(
        '-gp', '--gify',
        help='Deploy gify-panda service',
        required=False,
        action='store_true'
    )
    parser.add_argument(
        '-cp', '--counter',
        help='Deploy counter-panda service',
        required=False,
        action='store_true'
    )
    parser.add_argument('-a', '--all',action='store_true', help='Deploy all panda services')

    args = parser.parse_args()

    inventory_dir = 'dev'
    playbook = 'mybase.yml'

    if args.all:
        subprocess.call(['ansible-playbook', '-i', inventory_dir, '-t', 'gify-panda counter-panda', playbook])
    elif args.counter:
        subprocess.call(['ansible-playbook', '-i', inventory_dir, '-t', 'counter-panda', playbook])
    elif args.gify:
        subprocess.call(['ansible-playbook', '-i', inventory_dir, '-t', 'gify-panda', playbook])
