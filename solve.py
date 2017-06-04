
#=====================================================================================
#                       mymap.py
#                             by Ikko ota
#                             Last change 02 02 2017
#=====================================================================================

# subprocessでEDAをぶんまわすプログラム。
# 問題はtrainコーパス・パスの作成。全通りを作成し、ひとつのリストに納める。
# その後、それらをイテレーションしてtrain-EDAにぶち込む。

import os
import subprocess
import pandas as pd
import numpy as np
import pickle
from myaccu import myaccu

#-------------------------------------------------------------------------------------
#                        defs
#-------------------------------------------------------------------------------------

PR  = "~mori/link/resource/"
CWJ = "corpus/CWJ/auto/train.tree"
EHJ = "corpus/EHJ/auto/EHJ-train.tree"
NKN = "corpus/NKN/auto/NKN-train.tree"
NPT = "corpus/NPT/auto/NPT-train.tree"
RCP = "corpus/RCP/auto/RCP-train.tree"
JNL = "corpus/JNL/auto/JNL-train.tree"
TEST = "../resource/test/NKN-test.tree"


corpus = [PR+CWJ,PR+EHJ,PR+NPT,PR+RCP,PR+JNL]
cutoffs = ["01","02","04","08","16","32","64"]

result_cutoff = []

def gen_patterns():
    cases =[]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        cases.append([a,b,c,d,e])
    return cases

def detail(cases,corpus_list):
    groups = []
    for case in cases:
        group = []
        for (i,flag) in enumerate(case):
            if flag == 1:
                group.append('-c ' + corpus_list[i])
            else:
                continue
        groups.append(group)
    return groups   

#-------------------------------------------------------------------------------------
#                        preprocess
#-------------------------------------------------------------------------------------

patterns = gen_patterns()
groups = detail(patterns,corpus)
groups.pop(0) # (0,0,0,0,0)の削除
dict = {}
for i in range(31):
    dict[i] = groups[i]

with open('experdict.pickle','wb') as f: #コーパスの情報を取っておく
    pickle.dump(dict,f)

#-------------------------------------------------------------------------------------
#                        main
#-------------------------------------------------------------------------------------

for cutoff in cutoffs:
    result_group = []
    for g,group in enumerate(groups):
        group = ' '.join(group) ; g = str(g)
        args = ["train-eda",
                group,
                "-m " + "../model/group" + g + "_" + cutoff +".etm",
                "--cutoff",
                cutoff,
                "--left-to-right"]
        args  = ' '.join(args)
        print(args)
       # subprocess.run(args, shell=True)
        PRED = "../result/group"+ g + "_" + cutoff + ".eda"
        args = ' '.join(["eda","-m " + "../model/group" + g + "_" + cutoff +".etm","< " + TEST,"> " + PRED])
        print(args)
       # subprocess.run(args,shell=True)
        result_group.append(myaccu(TEST,PRED)) 
    result_cutoff.append(result_group) #グループ単位でくくった二重リスト

#-------------------------------------------------------------------------------------
#                        print & save
#-------------------------------------------------------------------------------------

result = np.array(result_cutoff)
print(result)
np.save('result.npy',result)

#result = pd.DataFrame(result_cutoff,index = cutoffs,columns = groups)
#result.to_csv('expr.csv')

#=====================================================================================
#                        END
#=====================================================================================
