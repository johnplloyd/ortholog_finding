print'''
Inputs:
	1 - Directory with FASTA groups
	2 - Output directory
	3 - .runcc name
'''
import os,sys

in_dir = os.path.abspath(sys.argv[1])
out_dir = os.path.abspath(sys.argv[2])
runcc_name = sys.argv[3]
if not runcc_name.endswith(".runcc"):
	runcc_name = runcc_name+".runcc"
runcc = open(runcc_name,"w")

for file in os.listdir(in_dir):
	if file.endswith(".fa"):
		runcc.write("module load MUSCLE;muscle -in %s/%s -out %s/%s.aln -maxiters 15\n" % (in_dir,file,out_dir,file))

runcc.close()