def linear_search(arr, target):
    
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
            


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    
    high = len(arr) -1
    
    while low <= high:
        # first get the mid point between t
        midpoint = (low + high ) //2 
        
        if target == arr[midpoint]:
            return midpoint
        if target < arr[midpoint]:
            high = midpoint - 1
        if target > arr[midpoint]:
            low = midpoint + 1
    return -1  # not found
