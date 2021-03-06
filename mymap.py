#=====================================================================================
#                       solve.csh
#                             by Ikko ota
#                             Last change 02 02 2017
#=====================================================================================

# 使い方：python mymap.py [元のテストファイル] [写像先のテストファイル]
# 意味： edaは時期によって微妙に文末処理が異なっている（！）
# ので、'-1 補助記号 UNK 0'を含む行を弾いてver.0.44の出力に合わせる必要があるというわけ。
#

import os
import sys

elem = sys.argv[1]
res = sys.argv[2]

#-------------------------------------------------------------------------------------
#                        main
#-------------------------------------------------------------------------------------

def mymap(pathA,pathB):
	f = open(pathA,'r')
	g = open(pathB,'w')
	for line in f:
		if '-1 補助記号 UNK 0' in line:
			continue
		else:
			g.write(line)
	f.close()
	g.close()

mymap(elem,res)

#=====================================================================================
#                        END
#=====================================================================================