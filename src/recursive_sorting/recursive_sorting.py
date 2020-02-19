import random
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # Elements is declaring how many values will be in the merged array
    elements = len( arrA ) + len( arrB )
    # this is creating an array with the length of your two arrays combined
    merged_arr = [] 
    # Compare the elements in arrA and arrB and sort them, returning merged arr
    # First pass will return lists with len==1 return those as a merged array
    test_arr = []
    print(arrA, "A")
    print(arrB, "B")       
    # First pass will return lists with len==1 return those as a merged array
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)
    while len(arrA) == 0 and len(arrB) > 0:
        if arrB[0] < merged_arr[0]:
            merged_arr.insert(0, arrB[0])
            arrB.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)
    while len(arrB) == 0 and len(arrA) > 0:
        if arrA[0] < merged_arr[0]:
            merged_arr.insert(0, arrA[0])
            arrA.pop(0)
        else:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        

        
        
        
        
    
        




        # else:
        #     if merged_arr[0] < arrB[0]:
                


        
    print(merged_arr, "merged arr before return")
    return merged_arr

arr5 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# arr5 = random.sample(range(200), 10)
# print(merge(arr5, arr6))
# def print_merge(arrA, arrB):
#     print("A", arrA)
#     print("B", arrB)
    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) < 2:
        return arr

    middle = len(arr)//2
    right = arr[0 : middle]
    left = arr[middle:]

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
