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
        return 'value not in array'

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
            return 'value not in array'

    return loc[0]

def pro_search(search_val, vec):
    '''
    This is just a copy of the solution for binary search from geekstogeeks.com that
    I typed up to make sure that I fully understand how it works. 
    This function, compared to my function search_numb, is much less complex.  
    This is because it changes the index of the array to search rather than "cutting" 
    it as it searches like my function search_numb above.
    '''
    # get the min and max indeces
    lo = 0
    hi = len(vec) - 1

    # create loop that continues until the search area is 0 terms
    while lo <= hi:

        mid = (hi + lo)//2 # get the midpoint index value, default to floor if even length array
        mid_val = vec[mid] # get the value at the midpoint
        
        if search_val > mid_val: # if search val is greater than midpoint, search higher half of array
            lo = mid + 1         # incriment up 1 from mid to search only what hasn't been searched
        
        elif search_val < mid_val: # if search val is less than midpoint, searvh lower half of array
            hi = mid - 1           # incriment down 1 from mid to search only what hasn't been searched
        
        else:                      # search_val == mid_val in this case, return location
            return mid
    
    return 'value not in array'

# generate the (sorted) list
lis        = np.arange(0,22,2)
search_val = 6

# test it out
a = search_numb(search_val, lis)
print(a)
b = pro_search(search_val, lis)
print(b)