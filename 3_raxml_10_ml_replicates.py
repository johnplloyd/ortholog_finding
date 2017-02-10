print'''
Inputs:
	1 - Directory with aligned files
	2 - Output .runcc name

Use the -wd option with qsub_hpc.py to set output directory
'''
import os,sys

in_dir = os.path.abspath(sys.argv[1])
runcc_name = sys.argv[2]
if not runcc_name.endswith(".runcc"):
	runcc_name = runcc_name+".runcc"
runcc = open(runcc_name,"w")

def num_seq(file_nm):
	ns = 0
	inp = open(file_nm)
	for line in inp:
		if line.startswith(">"):
			ns += 1
	inp.close()
	return ns

for file in os.listdir(in_dir):
	if file.endswith(".aln"):
		num_sequences = num_seq(in_dir+"/"+file)
		if num_sequences >= 4:
			runcc.write("module load raxml;raxmlHPC -s %s/%s -n %s -m PROTCATBLOSUM62 -# 10 -p 12345\n" % (in_dir,file,file))

runcc.close()
