# takes last element as pivot
# places the pivot element in its correct position in sorted array
# places smaller elements left of pivot
# places larger elements right of pivot


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # if the current element is smaller than pivot
        if arr[j] < pivot:
            # shift index of smaller element
            i = i + 1
            # swap the elements
            arr[i], arr[j] = arr[j], arr[i]

    # swapping the pivot with a index that is larger than itself
    # pivot in appropriate place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # return the index pivot is on
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        # pi is at its appropiate index due to partition function
        pi = partition(arr, low, high)

        # sorting sub arrays
        # sorting the elements smaller than pivot
        quickSort(arr, low, pi - 1)
        # sorting the elements larger than pivot
        quickSort(arr, pi + 1, high)


# testing
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is: ")
for i in range(n):
    print("%d" % arr[i])
