print'''
Inputs:
	1 - Directory with .split_og files
	2 - Output name
'''
import os,sys,fn

dir = os.path.abspath(sys.argv[1])
out_nm = sys.argv[2]

def clean_left_right(left_right_str):
	list = left_right_str.split(",")
	clean_list = []
	for item in list:
		if ":" not in item:
			clean_list.append(item)
		else:
			clean_item = item.split(":")[0]
			clean_list.append(clean_item)
	clean_str = ",".join(clean_list)
	return clean_str

def orth_groups(inp_file,out_file):
	inp = open(inp_file)
	# out = open(out_n,"w")
	for line in inp:
		if not line.startswith("NodeTaxa"):
			lineLst = line.strip().split("\t")
				# print lineLst
			if len(lineLst) == 4:
				nodeTaxa,dup_spe,left,right = lineLst
				if dup_spe == "0":
					clean_left = clean_left_right(left)
					clean_right = clean_left_right(right)
					out_file.write(clean_left+"\t"+clean_right+"\n")
			elif len(lineLst) == 3:
				nodeTaxa,dup_spe,left = lineLst
				if dup_spe == "0":
					print lineLst
					clean_left = clean_left_right(left)
					out_file.write(clean_left+"\n")
	inp.close()
	# out.close()

files_list = fn.get_files(dir,probe=".split_og",headtail="tail")
out = open(out_nm,"w")
for file in files_list:
	# print file
	orth_groups(file,out)
out.close()