#=====================================================================================
#                       lang-res.csh
#                           by Shinsuke Mori
#                           Last change : 29 April 2015
#=====================================================================================

# 機  能 : テキスト解析ツールのデータの設定
#
# 使用法 : source lang-res.csh
#
# 実  例 : source lang-res.csh
#
# 注意点 : UTF-8?


#-------------------------------------------------------------------------------------
#                       general variables
#-------------------------------------------------------------------------------------

set PR = ~mori/link/resource                      # PROJECT-ROOT

# General
set CWJ = corpus/CWJ/auto
set NKN = corpus/NKN/auto
set EHJ = corpus/EHJ/auto

# Target
set MMH = corpus/MMH/auto
set NPT = corpus/NPT/auto
set JNL = corpus/JNL/auto
set RCP = corpus/RCP/auto
set SGC = corpus/SGC/auto
set TWI = corpus/TWI/auto

# Test Only
set LSD = corpus/LSD/auto
set MPT = corpus/MPT/auto

set DICT = dict/auto


#-------------------------------------------------------------------------------------
#                       KyTea
#-------------------------------------------------------------------------------------

# テストデータ

set CWJ_KYTEA_TEST = ( $PR/$CWJ/test/ClassA-1-OC.wordpartfinekkci \
                       $PR/$CWJ/test/ClassA-1-OW.wordpartfinekkci \
                       $PR/$CWJ/test/ClassA-1-OY.wordpartfinekkci \
                       $PR/$CWJ/test/ClassA-1-PB.wordpartfinekkci \
                       $PR/$CWJ/test/ClassA-1-PM.wordpartfinekkci \
                       $PR/$CWJ/test/ClassA-1-PN.wordpartfinekkci )

set GEN_KYTEA_TEST = ( $PR/$NKN/NKN-test.wordNullNullkkci \
                       $PR/$EHJ/EHJ-test.wordNullNullkkci )

set ETC_KYTEA_TEST = ( $PR/$MMH/MMH-test.wordNullNullkkci \
                       $PR/$NPT/NPT-test.word \
                       $PR/$JNL/JNL-test.word \
                       $PR/$RCP/RCP-test.word \
                       $PR/$SGC/SGC-test.word \
                       $PR/$LSD/LSD.wordpartNullkkci \
                       $PR/$MPT/MPT.wordNullNullkkci \
                       $PR/$TWI/tweet-test.word )

set LRE_KYTEA_TEST = ( $PR/$NPT/NPT-test.word \
                       $PR/$RCP/RCP-test.word \
                       $PR/$TWI/tweet-test.word )

set KYTEA_TEST = ( $CWJ_KYTEA_TEST )


#-------------------------------------------------------------------------------------

# フルアノテーション

set CWJ_KYTEA_FULL = ( $PR/$CWJ/train/PB-train.wordpartfinekkci \
                       $PR/$CWJ/train/PM-train.wordpartfinekkci \
                       $PR/$CWJ/train/PN-train.wordpartfinekkci \
                       $PR/$CWJ/train/OC-train.wordpartfinekkci \
                       $PR/$CWJ/train/OW-train.wordpartfinekkci \
                       $PR/$CWJ/train/OY-train.wordpartfinekkci )

set CWJ_KYTEA_FULL = ( $PR/$CWJ/train/head100-PB-train.wordpartfinekkci \
                       $PR/$CWJ/train/head100-PM-train.wordpartfinekkci \
                       $PR/$CWJ/train/head100-PN-train.wordpartfinekkci \
                       $PR/$CWJ/train/head100-OC-train.wordpartfinekkci \
                       $PR/$CWJ/train/head100-OW-train.wordpartfinekkci \
                       $PR/$CWJ/train/head100-OY-train.wordpartfinekkci )

set GEN_KYTEA_FULL = ( $PR/$NKN/NKN-train.wordNullNullkkci \
                       $PR/$EHJ/EHJ-train.wordNullNullkkci )

set ETC_KYTEA_FULL = ( $PR/$MMH/MMH-train.wordNullNullkkci \
                       $PR/$NPT/NPT-train.word \
                       $PR/$JNL/JNL-train.word \
                       $PR/$RCP/RCP-train.word \
                       $PR/$SGC/SGC-train.word \
                       $PR/$SGC/joryu+kishi.wordpartkkci \
                       $PR/$SGC/kifu.wordpartkkci \
                       $PR/$LSD/LSD.wordpartNullkkci \
                       $PR/$MPT/MPT.wordNullNullkkci \
                       $PR/$TWI/tweet-train.word \
                       $PR/corpus/etc/auto/tahi-all.word \
                       $PR/corpus/etc/auto/neubig-full.wordpartNullkkci )


# Default Model (BCCWJ)
set KYTEA_FULL = ""
foreach FULL ( $CWJ_KYTEA_FULL )
    set KYTEA_FULL = "$KYTEA_FULL -full $FULL"
end

# Project Next NLP, Kagami Dist.
foreach FULL ( $GEN_KYTEA_FULL )
#    set KYTEA_FULL = "$KYTEA_FULL -full $FULL"
end

# 配布モデル (2014/10/18)
foreach FULL ( $ETC_KYTEA_FULL )
#    set KYTEA_FULL = "$KYTEA_FULL -full $FULL"
end
foreach FULL ( $CWJ_KYTEA_TEST $GEN_KYTEA_TEST $ETC_KYTEA_TEST )
#    set KYTEA_FULL = "$KYTEA_FULL -full $FULL"
end

# 以下、ザ変問題の修正が必要(追加すると読み推定精度があがるかも)
#                  -full $PR/$NKN/NKN.wordkkci \
#                  -full $PR/$EHJ/EHJ.wordkkci \


#-------------------------------------------------------------------------------------

# 部分的アノテーション

set KYTEA_PART = ""

set KYTEA_PART = "-part $PR/corpus/etc/auto/mori-part.wordkkci \
                  -part $PR/corpus/NPT/auto/NTCIR-part.word \
                  -part $PR/corpus/RCP/auto/Aji-0.10-00002-part.word \
                  -part $PR/corpus/RCP/partial/Aji-active-001.wann \
                  -part $PR/corpus/RCP/partial/Aji-active-002.wann \
                  -part $PR/corpus/MNN/auto/MNN-part.word \
                  -part $PR/$RCP/05-07-all.kpartial \
                 "
# Project Next NLP
#set KYTEA_PART = ""

# Kagami Dist
#set KYTEA_PART = ""

# LREC2014(?)
set KYTEA_PART = ""
#set KYTEA_PART = "-part /home/mori/work/RecipeText2Flow/recipe-ne-data/05-07-64oc.kpartial"

# Add ANPI-NLP


#-------------------------------------------------------------------------------------

# 辞書

set KYTEA_DICT = ""

# 配布モデル (2014/08/??)
#set KYTEA_DICT = "-dict $PR/$DICT/unidic.wordpartkkci \
#                  -dict $PR/$DICT/name-f.wordkkci \
#                  -dict $PR/$DICT/name-l.wordkkci \
#                  -dict $PR/$DICT/number.wordkkci \
#                  -dict $PR/$DICT/sign.word \
#                  -full $PR/$DICT/player.wordkkci \
#                  -full $PR/$DICT/tokunaga.wordkkci \
#                  -dict $PR/$DICT/LSD-Atok.dict \
#                  -dict $PR/$DICT/filtered-NKD-Patro.dict \
#                 "

# Kagami Dist
#set KYTEA_DICT = "-dict $PR/$DICT/unidic.wordpartkkci \
#                  -dict $PR/$DICT/name-f.wordkkci \
#                  -dict $PR/$DICT/name-l.wordkkci \
#                  -dict $PR/$DICT/number.wordkkci \
#                 "

#                  -dict ~/link/resource/dict/auto/UTF8-NKD-Patro.comp \

# LREC2014(?)
#                  -dict /home/mori/work/RecipeText2Flow/recipe-ne-data/05-07.dict \

# Add unit/*


#-------------------------------------------------------------------------------------
# 未知語モデル (subword)

#set KYTEA_SUBW = "-subword $PR/dict/tankan/auto/tankan.wordNULLNULLkkci \
#                 "
set KYTEA_SUBW = ""


#-------------------------------------------------------------------------------------
#                       EDA
#-------------------------------------------------------------------------------------

# HP
set EDA_FULLtest =(-c $PR/$CWJ/train.tree \
              -c $PR/$EHJ/EHJ-train.tree \
              -c $PR/$NPT/NPT-train.tree \
              -c $PR/$RCP/RCP-train.tree \
              -c $PR/$JNL/JNL-train.tree \
              )

set EDA_4cp = (-c $PR/$CWJ/train.tree \
              -c $PR/$EHJ/EHJ-train.tree \
              -c $PR/$NPT/NPT-train.tree \
              -c $PR/$RCP/RCP-train.tree \
              )

set EDA_3cp = (-c $PR/$CWJ/train.tree \
              -c $PR/$EHJ/EHJ-train.tree \
              -c $PR/$NPT/NPT-train.tree \
              )

set EDA_2cp = (-c $PR/$CWJ/train.tree \
              -c $PR/$EHJ/EHJ-train.tree \
              )

set EDA_1cp = (-c $PR/$CWJ/train.tree)

# Project Next NLP
#set EDA_FULL = "-c $PR/$JNL/train.tree \
#               "
#-c $PR/$CWJ/train.tree \

# 配布モデル (2014/07/25)
set EDA_FULL = (-c $PR/$CWJ/train.tree \
               -c $PR/$EHJ/EHJ-train.tree \
               -c $PR/$NKN/NKN-train.tree \
               -c $PR/$NPT/NPT-train.tree \
               -c $PR/$JNL/JNL-train.tree \
               -c $PR/$RCP/RCP-train.tree \
               -c $PR/$CWJ/test.tree \
               -c $PR/$EHJ/EHJ-test.tree \
               -c $PR/$NKN/NKN-test.tree \
               -c $PR/$NPT/NPT-test.tree \
               -c $PR/$JNL/JNL-test.tree \
               -c $PR/$RCP/RCP-test.tree \
              )

#set EDA_FULL = "-c $PR/$CWJ/test.tree \
#                -c $PR/$CWJ/train.tree \
#                -c $PR/$EHJ/train.tree \
#                -c $PR/$NKN/train.tree \
#                -c $PR/$RCP/train.tree \
#                -c $PR/$JNL/train.tree \
#                -c $PR/$NPT/NPT-train.tree \
#		"

#-------------------------------------------------------------------------------------

# 部分的アノテーション

# 精度が下がる (要詳細確認)
#set EDA_PART = "-c $PR/corpus/EDR/partial/EDR.tree \
#                -c $PR/corpus/KUC/data/seg/train.tree \
#                "

# 配布モデル (2014/07/25)
set EDA_PART = ""


#-------------------------------------------------------------------------------------

# テストデータ

#set EDA_TEST = ( $PR/$CWJ/OC-test-01-05.tree \
#                 $PR/$CWJ/OW-test-01-05.tree \
#                 $PR/$CWJ/OY-test-01-05.tree \
#                 $PR/$CWJ/PB-test-01-05.tree \
#                 $PR/$CWJ/PM-test-01-05.tree \
#                 $PR/$CWJ/PN-test-01-05.tree \
#                 $PR/$EHJ/EHJ-test.tree \
#                 $PR/$NKN/NKN-test.tree \
#                 $PR/$RCP/RCP-test.tree \
#                 $PR/$JNL/JNL-test.tree \
#                 $PR/$NPT/NPT-test.tree \
#           )

set CWJ_EDA_TEST = ( $PR/$CWJ/test/ClassA-1-OC.tree \
                     $PR/$CWJ/test/ClassA-1-OW.tree \
                     $PR/$CWJ/test/ClassA-1-OY.tree \
                     $PR/$CWJ/test/ClassA-1-PB.tree \
                     $PR/$CWJ/test/ClassA-1-PM.tree \
                     $PR/$CWJ/test/ClassA-1-PN.tree )

set EDA_TEST = ( $CWJ_EDA_TEST \
                 $PR/$EHJ/EHJ-test.tree \
                 $PR/$NKN/NKN-test.tree \
                 $PR/$NPT/NPT-test.tree \
                 $PR/$JNL/JNL-test.tree \
                 $PR/$RCP/RCP-test.tree \
               )


#=====================================================================================
#                       END
#=====================================================================================
