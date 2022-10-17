import os
import sys
import textwrap
my_dict2={}
with open('../metadata') as file:
    for line in file:
        if 'data' in line:
            continue
        my_dict2[line.split('\t')[0].strip().replace('.bam','')]=line.split('\t')[1].strip()
CWD=os.getcwd().split("/")
CWD=[i for i in CWD if "TCGA" and ".d" in i]
CWD=CWD[0].replace('.d','')
sequencing_center=my_dict2[CWD].split()[0]
CWD="-".join(CWD.split("-")[0:4])
fasta=sys.argv[1]
with open(fasta) as file:
        kk=file.readlines()
my_dict={}
length=0
n=0
jj=1
for i in kk:
        if (i.startswith('>')):
                n+=1
                id_1=i.strip()
                my_dict[id_1]=""
        if (not i.startswith('>')) and  (jj == n):
                my_dict[id_1]=my_dict[id_1]+i.strip()
        if jj != n:
                jj=n



with open('test_contig','w') as file:
        n=0
        for i,l in my_dict.items():
            n+=1
            if len(l) >= 0:
                name=i.split()[0].lstrip('>')
                i=f'>{CWD}-{n}-Blood-{sequencing_center}'
                file.writelines([i.strip(),'\n',l,'\n'])
