import os

path = "F:\桶蛋白\omp31\omp31pdb" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []

aa_codes = {
    'ALA':'A','CYS':'C','ASP':'D','GLU':'E',
    'PHE':'F','GLY':'G','HIS':'H','LYS':'K',
    'ILE':'I','LEU':'L','MET':'M','ASN':'N',
    'PRO':'P','GLN':'Q','ARG':'R','SER':'S',
    'THR':'T','VAL':'V','TYR':'Y','TRP':'W'
}
seq = ''

for file in files:
    name = file.split(".")
    for line in open(file):
        if line[0:6] =="SEQRES":
            columns = line.split()
            for resname in columns[4:]:
                seq = seq + aa_codes[resname]
    i = 0
    print(">"+name[0])
    while i < len(seq) :
        print(seq[i:i+64])
        i =i+64
    seq = ''
