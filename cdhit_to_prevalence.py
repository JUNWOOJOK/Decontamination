import sys
import collections
input=sys.argv[1]
from itertools import groupby
with open(input) as file:
    zxc=file.readlines()
aaa=collections.defaultdict()
my_dict={}
zzz=[list(k) for i,k in  groupby(zxc,lambda x:'Cluster' in x) if not i]

def cluster_processing_to_dict(list):
    list_a=[i.split('>')[1].split('...')[0] for i in list]
    for k in list:
        if "*" in k:
            name=k.split('>')[1].split('...')[0]
    aaa[name]=list_a
for i in zzz:
    cluster_processing_to_dict(i)

list_total=[]
for i in aaa.values():
    list_total+=i

total_tissue_count=len(set(['-'.join(i.split('-')[0:4]) for i in list_total if 'Normal' in i or 'Tumor' in i]))
total_blood_count=len(set(['-'.join(i.split('-')[0:4]) for i in list_total if ('Blood') in i]))

for key,value in aaa.items():
    Tissue_count=len(set(['-'.join(i.split('-')[0:4]) for i in value if 'Tumor' in i or 'Normal' in i]))
    Blood_count=len(set(['-'.join(i.split('-')[0:4]) for i in value if 'Blood' in i]))
    my_dict[str(key)]=[Tissue_count/total_tissue_count,Blood_count/total_blood_count]

for i,l in my_dict.items():
    print(i,l[0],l[1],sep="\t")
