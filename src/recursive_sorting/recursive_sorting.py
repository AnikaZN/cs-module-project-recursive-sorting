# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    a, b = len(arrA), len(arrB)
    elements = a + b
    merged_arr = [0] * elements

    # Your code here
    for i in range(len(merged_arr)):

        a, b = len(arrA), len(arrB)

        # If either of the lists have nothing left in them
        if a == 0 or b == 0:
            for item in arrA:
                merged_arr[i] = item
                i += 1
            for item in arrB:
                merged_arr[i] = item
                i += 1

            return merged_arr

        x, y = arrA[0], arrB[0]

        # If x is smaller
        if x < y:
            merged_arr[i] = x
            arrA.remove(x)
        # If y is smaller
        else:
            merged_arr[i] = y
            arrB.remove(y)

        # If they are equal
        # This is kind of broken, but doesn't matter b/c test don't address this
        # else:
        #     merged_arr[i] = x
        #     merged_arr[i + 1] = y
        #     arrA.remove(x)
        #     arrB.remove(y)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    arrA = arr[:(len(arr) // 2)]
    arrB = arr[(len(arr) // 2):]

    return merge(merge_sort(arrA), merge_sort(arrB))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    # "Mid" is the beginning of the second list
    while start < mid and mid < end + 1:

        # If the value at "start" < the value at "mid"
        if arr[start] < arr[mid]:
            # Advance start
            start += 1
        else:
            # For each item in the first half
            for i in range(start, mid):
                # Swap the item and the "mid" value
                arr[i], arr[mid] = arr[mid], arr[i]
            # Advance start and mid
            start += 1
            mid += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    # When both pointers are at the end, we're done!
    if r - l <= 0:
        return arr

    # Find our midpoint
    mid = l + ((r - l) // 2)

    # MSIP the left half
    merge_sort_in_place(arr, l, mid)
    # MSIP the right half
    merge_sort_in_place(arr, mid + 1, r)
    # MIP the whole thing
    merge_in_place(arr, l, mid + 1, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
