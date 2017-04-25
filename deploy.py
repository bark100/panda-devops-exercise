#!/usr/bin/env python

import argsparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--service', type=str, help='Services to deploy, seperated by comma', required=True,nargs='+')
    parser.add_argument('-s', '--secondarg', default = '',
                        help ='Second Argument')
    parser.add_argument('-t', '--thirdarg', default = '',
                        help ='Third Argument')
    args = parser.parse_args()
    service = args.service[0].split(",")
    print args
    
    args.service
    
    ansible-playbook mybase.yml -t gify-panda -i dev

   
    main(args.firstarg, args.secondarg, args.thirdarg)
