# Austin Richards 12/27/20 10:55

import numpy as np

# generate the (already sorted) list
n   = 50
lis = np.zeros(n)

for i in range(0,n):
    lis[i] = (i+1)*2  # every other value starting with 2, up to 100

