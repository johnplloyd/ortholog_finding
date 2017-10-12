print'''
Inputs:
	1 - Directory with .reconciled files
'''

import os, sys

dir = os.path.abspath(sys.argv[1])


for file in os.listdir(dir):
    if file.endswith('.reconciled'):
        os.system('python /mnt/home/lloydjo1/scripts/Shiu_Scripts/TreeUtility.py -f parse_notung -t %s/%s' % (dir,file))

