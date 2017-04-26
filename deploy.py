#!/usr/bin/env python

import argparse # manage script arguments
import subprocess # we use subprocess to saftely execute ansible
import sys # handle script decleration

def main (argv=None): # define main function

        parser = argparse.ArgumentParser(description='Panda services deployer tool version 0.1') # declare instance of argparse
        parser.add_argument( # deploy gify panda
            '-gp', '--gify',
            help='Deploy gify-panda service',
            required=False,
            action='store_true'
        )
        parser.add_argument( # deploy counter panda
            '-cp', '--counter',
            help='Deploy counter-panda service',
            required=False,
            action='store_true'
        )
        parser.add_argument('-a', '--all',action='store_true', help='Deploy all panda services') # deploy all panda services
    
        args = parser.parse_args()
        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(1)

        inventory_dir = 'dev' # hardcode inventory and playbook to simplify script execution
        playbook = 'mybase.yml'
    
        if args.all:
            subprocess.call(['ansible-playbook', '-i', inventory_dir, '--tags=gify-panda,counter-panda', playbook]) # call ansible
        elif args.counter:
            subprocess.call(['ansible-playbook', '-i', inventory_dir, '-t', 'counter-panda', playbook])
        elif args.gify:
            subprocess.call(['ansible-playbook', '-i', inventory_dir, '-t', 'gify-panda', playbook])


if __name__ == '__main__': # excute code only if script was run directly and not via import
    main(sys.argv[1:])
