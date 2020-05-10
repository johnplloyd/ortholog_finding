print'''
Inputs:
	1 - Directory with .midpoint files
	2 - Output directory
	3 - Species tree
	4 - Notung jar location
'''
import os,sys

dir_in = os.path.abspath(sys.argv[1])
dir_out = os.path.abspath(sys.argv[2])
species_tree = sys.argv[3]
notung_jar_loc = sys.argv[4]

for file in os.listdir(dir_in):
    if file.endswith('.midpoint'):
        os.system('java -jar %s '\
		'-g %s/%s -s %s --reconcile -speciestag prefix -edgeweights length '\
		'--outputdir %s' % (notung_jar_loc,dir_in,file,species_tree,dir_out))

