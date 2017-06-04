#=====================================================================================
#                       Run_RDA.py
#                             by Ikko ota
#                             Last change 02 02 2017
#=====================================================================================

# subprocessでEDAをぶんまわすプログラム。
# 問題はtrainコーパス・パスの作成。全通りを作成し、ひとつのリストに納める。
# その後、それらをイテレーションしてtrain-EDAにぶち込む。

import os
import sys
import subprocess
import glob
import pandas as pd
import numpy as np
import pickle
from myaccu import myaccu

#-------------------------------------------------------------------------------------
#                        defs
#-------------------------------------------------------------------------------------

OC = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/OC*.tree")
OW = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/OW*.tree")
OY = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/OY*.tree")
PB = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/PB*.tree")
PM = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/PM*.tree")
PN = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/PN*.tree")

TEST = "/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/test/sakata-2017-02.tree"

corpus = [OC,OW,OY,PB,PM,PN]
cutoffs = ["01","02","04","08","16","32","64"]

result_cutoff = []

def gen_patterns():
    cases =[]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            cases.append([a,b,c,d,e,f])
    return cases

def grouping(cases,corpus_list):
    groups = []
    for case in cases:
        group = []
        for (i,flag) in enumerate(case):
            if flag == 1:
                group.append(corpus_list[i])
            else:
                continue
        groups.append(group)
    return groups   

def cmdize(groups):
    cmds =[]
    for group in groups:
        cmd = []
        for corpus in group:
            for elem in corpus:
                cmd.append('-c '+ elem)
        cmds.append(cmd)
    return cmds

#-------------------------------------------------------------------------------------
#                        preprocess
#-------------------------------------------------------------------------------------

patterns = gen_patterns()
groups = grouping(patterns,corpus)
groups.pop(0)  # (0,0,0,0,0)の削除
groups = cmdize(groups)  # -cを付与

dict = {}
for i in range(63):
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
        #print(args)
        #subprocess.run(args, shell=True)
        PRED = "../result/group"+ g + "_" + cutoff + ".eda"
        args = ' '.join(["eda","-m " + "../model/group" + g + "_" + cutoff +".etm","< " + TEST,"> " + PRED])
        #print(args)
        #subprocess.run(args,shell=True)
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
