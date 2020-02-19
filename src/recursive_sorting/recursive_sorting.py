import random
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # Elements is declaring how many values will be in the merged array
    elements = len( arrA ) + len( arrB )
    # empty array to merge the values that are being passed in
    merged_arr = [] 
    # Compare the elements in arrA and arrB and sort them, returning merged arr  

    # Loops through both arrays while they each have elements in them and compares
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            del arrA[0]
        else:
            merged_arr.append(arrB[0])
            del arrB[0]
    # Loops through arrB while A is empty and compares it againse the values input into merged Arr
    while len(arrA) == 0 and len(arrB) > 0:
        if arrB[0] < merged_arr[0]:
            merged_arr.insert(0, arrB[0])
            del arrB[0]
        else:
            merged_arr.append(arrB[0])
            del arrB[0]
    # Loops through arrA while B is empty and compares it againse the values input into merged Arr
    while len(arrB) == 0 and len(arrA) > 0:
        if arrA[0] < merged_arr[0]:
            merged_arr.insert(0, arrA[0])
            del arrA[0]
        else:
            merged_arr.append(arrA[0])
            del arrA[0]

        
    print(merged_arr, "merged arr before return")
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Base case to check if the arr is a single element or empty
    if len(arr) < 2:
        return arr

    # splits the array indefinitely, cancels when it hits base case
    middle = len(arr)//2
    right = arr[0 : middle]
    left = arr[middle:]

    # calls the merge_sort recursively passing in the arrays returned from merge_sort once it hits len 1
    merged_arr = merge(merge_sort(right), merge_sort(left))
    return merged_arr
    
print(arr5)
print(merge_sort(arr5), 'Merge Sort')

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
