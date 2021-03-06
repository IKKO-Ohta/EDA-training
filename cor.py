#=====================================================================================
#                       cor.py
#                             by Ikko ota
#                             Last change 02 06 2017
#=====================================================================================

# グループ間の類似度と精度の相関を検証する。
# $cor.py 精度.npy sim.npy

import sys
import numpy as np

accu = np.load(sys.argv[1])[1]
sim = np.load(sys.argv[2])
print(np.corrcoef(accu, sim)[0, 1])
#=====================================================================================
#                        END
#=====================================================================================
