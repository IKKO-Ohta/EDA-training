import sys
import numpy as np

accu = np.load(sys.argv[1])[1]
sim = np.load(sys.argv[2])
print(np.corrcoef(accu, sim)[0, 1])
