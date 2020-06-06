def partition(arr):
    left = []
    right = []
    pivot = arr[0]

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right


def quicksort(arr):

    if len(arr) == 0:
        return arr

    # Partition into left/pivot/right
    left, pivot, right = partition(arr)

    return quicksort(left) + pivot + quicksort(right)
