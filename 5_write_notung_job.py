print'''
Inputs:
	1 - Directory with .midpoint files
	2 - Output directory
	3 - Species tree
'''
import os,sys

dir_in = os.path.abspath(sys.argv[1])
dir_out = os.path.abspath(sys.argv[2])
species_tree = sys.argv[3]

for file in os.listdir(dir_in):
    if file.endswith('.midpoint'):
        os.system('java -jar /mnt/home/lloydjo1/bin/Notung-2.6/Notung-2.6.jar '\
		'-g %s/%s -s %s --reconcile -speciestag prefix -edgeweights length '\
		'--outputdir %s' % (dir_in,file,species_tree,dir_out))

