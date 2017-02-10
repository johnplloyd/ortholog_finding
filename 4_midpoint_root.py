print'''
Inputs:
	1 - Directory with trees
	2 - Output directory
'''
import os, sys

dir_in = os.path.abspath(sys.argv[1])
dir_out = os.path.abspath(sys.argv[2])

def retree(directory,inp_file):
	f = os.popen('retree', 'w')
	f.write('Y\n')#setting correct
	f.write('%s/%s\n' % (directory,inp_file))#tree name
	# f.write('%s%s\n' % (directory,inp_file))#tree name
	f.write('M\n')#midpoint
	f.write('W\n')#write
	f.write('R\n')#rooted? yes
	f.write('Q\n')#quit

for file in os.listdir(dir_in):
	print file
	if file.endswith(".fa.aln"):
		# print "\tyep"
		retree(dir_in,file)
		new_file = dir_out+"/"+file+'.midpoint'
		os.system('mv outtree %s' % (new_file))