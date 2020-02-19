import random
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        # Puts i(index) into a manipulatable variable
        cur_index = i
        # Another manipulatable variable for i
        small_index = cur_index
        # Save the current value for the element at i 
        value = arr[cur_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # Loop through the array again, allowing you to compare indexes
        for num in range(cur_index, len(arr)):
            # Compare values at indexes declared in different loops
            if arr[num] < arr[small_index]:
                # Changing manipulatable index to move the sort along.
                small_index = num
        # Swaps values
        arr[cur_index] = arr[small_index]
        arr[small_index] = value


    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    passes = 1
    # Declare your loop for the value that you will be using to compare adjacent elements
    for i in range(len(arr) - 1):
        # Runs another loop to compare adjacent elements
        for k in range(len(arr) - 1):
            #Compares adjacent elements 
            if arr[k] > arr[k + 1]:
                # Allows for swapping
                value = arr[k]
                #Swap
                arr[k] = arr[k + 1]

    
            

    return arr
    
arr5 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
bubble_sort(arr5)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr