# Austin Richards 12/27/20 10:55

import numpy as np

def search_numb(search_val, vec):
    '''
    search_numb takes a number and looks for it in vec using binary search
    inputs:
        vec: a vector of numbers in ascending order
        search_val: an integer or float 
    outputs:
        loc: location of the value
    '''
    n          = len(vec)
    center     = floor( n / 2 )
    center_val = vec[center]

    while center_val != search_val:
        n          = len(vec)
        center     = int(floor(n/2))
        center_val = vec[center]

        if search_val < center_val:
            vec = vec[0:center]
        else:
            vec = vec[center:n]


# generate the (sorted) list
n   = 50
lis = np.zeros(n)

for i in range(0,n):
    lis[i] = (i+1)*2  # every other value up to 2n starting with 2

print('Enter a value to search from 0 to', n)
search_val = input()  # take an input from the user, put it into search value

