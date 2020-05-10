print'''
Inputs:
	1 - Directory with .reconciled files
	2 - TreeUtility.py location
'''

import os, sys

dir = os.path.abspath(sys.argv[1])
TreeUtility_loc = sys.argv[2]

for file in os.listdir(dir):
    if file.endswith('.reconciled'):
        os.system('python %s -f parse_notung -t %s/%s' % (TreeUtility_loc,dir,file))

