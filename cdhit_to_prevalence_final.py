import sys
import collections
import os
list_kkk=[]

input=sys.argv[1]
blood_dir=sys.argv[2]
tissue_dir=sys.argv[3]

blood_file=[i.strip() for i in os.listdir(blood_dir) if 'TCGA' in i]
tissue_file=[i.strip() for i in  os.listdir(tissue_dir) if 'TCGA' in i]

blood_id=list(set(['-'.join(i.split('-')[0:3]) for  i in blood_file]))
tissue_id=list(set(['-'.join(i.split('-')[0:3]) for  i in tissue_file]))


total_id=blood_id+tissue_id
x=collections.Counter(total_id)





for i,l in x.items():
    if l==2:
        list_kkk.append(i.strip())

total_count=len(list_kkk)



from itertools import groupby
with open(input) as file:
    zxc=file.readlines()
aaa=collections.defaultdict()
my_dict={}
zzz=[list(k) for i,k in  groupby(zxc,lambda x:'Cluster' in x) if not i]
#zzz=[i for i in zzz if zzz]
def cluster_processing_to_dict(list):
    list_a=[i.split('>')[1].split('...')[0] for i in list]
    for k in list:
        if "*" in k:
            name=k.split('>')[1].split('...')[0]
    try:
        aaa[name]=list_a
    except:
        pass
for i in zzz:
    cluster_processing_to_dict(i)










for key,value in aaa.items():
    Tissue_count=len(set(['-'.join(i.split('-')[0:3]) for i in value if 'Tumor' in i or 'Normal' in i or 'Tissue' in i and ('-'.join(i.split('-')[0:3]) in list_kkk)]))
    Blood_count=len(set(['-'.join(i.split('-')[0:3]) for i in value if 'Blood' in i and ('-'.join(i.split('-')[0:3]) in list_kkk)]))
    my_dict[str(key)]=[Tissue_count/total_count,Blood_count/total_count]


for i,l in my_dict.items():
    print(i,l[0],l[1],sep="\t")

