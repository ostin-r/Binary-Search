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
    center_val = 0
    n = float('Inf')

    while center_val != search_val or n > 1:
        n          = len(vec)
        center     = int(np.floor(n/2))
        center_val = int(vec[center])
        print(center_val)
        print(search_val)

        if search_val < center_val:
            vec = vec[0:center]
        else:
            vec = vec[center:n]
        print(vec)
    
    if center_val == search_val:
        return center
    else:
        return 'value not in list'


# generate the (sorted) list
n   = 10
lis = np.zeros(n)

for i in range(0,n):
    lis[i] = ( i + 1 ) * 2  # every other value up to 2n starting with 2

search_val = 16  # search value

# call the function
a = search_numb(search_val, lis)
print(a)