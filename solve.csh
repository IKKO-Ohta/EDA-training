#=====================================================================================
#                       solve.csh
#                             by Ikko ota
#                             Last change 02 02 2017
#=====================================================================================

# 使い方：csh solve.csh

#-------------------------------------------------------------------------------------
#                        set variables
#-------------------------------------------------------------------------------------

source lang-res.csh
set corpuses = ("$EDA_FULLtest")
set cutoff_nums = (08)

#-------------------------------------------------------------------------------------
#                        main
#-------------------------------------------------------------------------------------

echo "processing..." > log.txt

foreach num (`seq 1 $#corpuses`)
  foreach cutoff_num ($cutoff_nums)

    set MODEL = ./up/"$num"_"$cutoff_num".ebm
    echo "        train-eda $corpuses[$num] -F feat.txt -m $MODEL --cutoff $cutoff_num --left-to-right"
    train-eda $corpuses[$num] -m $MODEL --cutoff $cutoff_num --left-to-right

   # set TEST = ../resource/test/NKN-test.tree
   # set PRED = ../result/0.3.5_group"$num"_"$cutoff_num".tree
   # echo "    eda -m $MODEL < $TEST > $PRED"
   # eda -m $MODEL < $TEST > $PRED                                                                                                                                                     

    #echo "    python myaccu.py $TEST $PRED >> ../result/result.txt"
    #echo "$TEST $PRED" >> ../result/result.txt
    #python myaccu.py $TEST $PRED >> ../result/result.txt
    echo "    "
  end
  echo DONE
end

#=====================================================================================
#                        END
#=====================================================================================
