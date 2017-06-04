#!/bin/csh
#=====================================================================================                              
#                       solve.csh                                                                                   
#                             by Ikko ota                                                                           
#                             Last change 02 02 2017                                                                
#=====================================================================================                              

# 使い方：csh solve.csh

#-------------------------------------------------------------------------------------                              
#                        set variables                                                                              
#-------------------------------------------------------------------------------------                              

set group = $argv[1]
set num = $argv[2]
set cutoff_num = $argv[3]

#-------------------------------------------------------------------------------------                              
#                        main                                                                                       
#-------------------------------------------------------------------------------------                              

set MODEL = ../model/group"$num"_"$cutoff_num".etm
echo "    train-eda $group -m $MODEL --cutoff $cutoff_num --left-to-right"                                                                       
train-eda $group -m $MODEL --cutoff $cutoff_num --left-to-right 

set TEST =  ../resource/test/NKN-test.tree
set PRED = ../result/group"$num"_"$cutoff_num".eda
echo "    eda -m $MODEL < $TEST > $PRED"                                   
eda -m $MODEL < $TEST > $PRED                                            

echo "    python myaccu.py $TEST $PRED >> ../result/result.txt"
echo "$TEST $PRED" >> ../result/result.txt
python myaccu.py $TEST $PRED >> ../result/result.txt

echo "DONE"


#=====================================================================================
#                        END
#=====================================================================================
