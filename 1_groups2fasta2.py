print'''
Inputs:
	1 - OrthoMCL groups file
	2 - Fasta file
	3 - Taxa, comma-delimited
	4 - Output directory

It is assumed that the IDs in each file are identical
'''
import os,sys

orthomcl_file = sys.argv[1]
fasta_file = sys.argv[2]
taxa_list = sys.argv[3].split(",")
output_dir = os.path.abspath(sys.argv[4])

def fasta2dict(file):
	inp = open(file)
	dict = {}
	id = None
	seq = ""
	for line in inp:
		if line.startswith(">"):
			if id != None:
				dict[id] = seq
			seq = ""
			id = line.strip().replace(">","")
		else:
			seq = seq+line.strip()
	dict[id]=seq
	inp.close()
	return dict

def all_taxa(list,str):
	all_present = True
	for item in list:
		if item not in str:
			all_present = False
	return all_present

def groups2fasta(file,taxa_lst,dict,dir):
	inp = open(file)
	out_l = open(file+".lost","w")
	for line in inp:
		group_ids = line.strip().split(":")
		ids = group_ids[1].split("\t")
		# print ids
		# print group_ids[1]
		all_present = all_taxa(taxa_lst,group_ids[1])
		# print all_present
		if all_present == False:
			for id in ids:
				out_l.write(id+"\n")
		else:
			if len(ids) > 2:
				group = group_ids[0]
				# print group
				out = open(dir+"/"+group.lower()+".fa","w")
				for id in ids:
					if id != "":
						# print id
						seq = dict[id]
						out.write(">"+id+"\n"+seq+"\n")
				out.close()
	out_l.close()

fasta_dict = fasta2dict(fasta_file)
groups2fasta(orthomcl_file,taxa_list,fasta_dict,output_dir)
