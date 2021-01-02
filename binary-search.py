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
    n          = len(vec)               # initialize vector length req'd for loop
    center_val = -float('Inf')          # initialize center_val to force while loop to begin 
    loc        = np.arange(len(vec))    # vector to track location as vec gets split
    max_val    = np.max(vec)            
    min_val    = np.min(vec)

    # check value is in the sorted list
    if search_val > max_val or search_val < min_val:
        return 'value not in list'

    # continue to split the list until the center value is what we are searching for
    while center_val != search_val:
        n          = len(vec)
        center     = int(np.floor(n/2))
        center_val = vec[center]

        if search_val < center_val:
            vec = vec[0:center]
            loc = loc[0:center]
        else:
            vec = vec[center:n]
            loc = loc[center:n]

        if n < 2 and center_val != search_val:
            return 'value not in list'

    return loc[0]

def pro_search(search_val, vec):
    '''
    After glancing over the solution for binary search offered on geekstogeeks.com,
    I attempt to implement it here from memory.  This function, compared to my function
    search_numb, is less complex.  This is because it changes the index of the array
    to search rather than "cutting" it as it searches.
    '''
    # get the min and max indeces
    lo = 0
    hi = len(vec) - 1

    # create loop that continues until len(vec) = 0
    while lo <= hi:

        mid = (hi + lo)//2 # get the midpoint index value, default to floor if even array
        mid_val = vec[mid] # get the value at the midpoint
        
        if search_val > mid_val:
            lo = mid

        elif search_val < mid_val:
            hi = mid
        
        else:
            return mid

# generate the (sorted) list
lis        = np.arange(0,22,2)
search_val = 12

a = search_numb(search_val, lis)
print(a)