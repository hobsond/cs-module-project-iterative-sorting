def linear_search(arr, target):
    
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
            


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # set low and hight to create the index boundaries
    low = 0
    
    high = len(arr) -1
    
    while low <= high:
        # first get the mid point between t
        midpoint = (low + high ) //2 
        # if target is the midpoint then the search is true
        if target == arr[midpoint]:
            return midpoint
        # if the target is less than the mid point
        # you know that the target is not equal to the midpoint and has to be less than it 
        # you will now set the high to to the index of before the current mid 
        # so that when the loop repeats it cuts of anything higher than the midmpoint
        if target < arr[midpoint]:
            high = midpoint - 1
        if target > arr[midpoint]:
            low = midpoint + 1
    return -1  # not found
