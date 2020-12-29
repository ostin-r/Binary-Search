# Austin Richards 12/27/20 10:55

import numpy as np

def search_numb(search_val, vec):
    '''
    search_numb takes a number and looks for it in vec using binary search
    inputs:
        vec: a vector of numbers in ascending order
        search_val: an integer or float 
    outputs:
        center: location of the value
    '''
    n          = float('Inf')
    center_val = 0
    loc        = np.arange(len(vec))

    while center_val != search_val:
        n          = len(vec)
        center     = int(np.floor(n/2))
        center_val = int(vec[center])

        if search_val < center_val:
            vec = vec[0:center]
            loc = loc[0:center]
        else:
            vec = vec[center:n]
            loc = loc[center:n]
    
    if center_val == search_val:
        return loc[0]
    else:
        return 'value not in list'


# generate the (sorted) list
loc        = np.arange(0,11)
lis        = np.arange(0,11)
search_val = 10
print(loc)
print(lis)

a = search_numb(search_val, lis)
print(a)