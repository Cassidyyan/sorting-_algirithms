# Long bubble sort
# iterates through a list bu tapping into indexes, comparing two indexes at a time and swapping if
# the index ahead [i+1] is greater than [i]


def bubble_sort(array):
    # the -1,0,-1 allows sys to run
    for pass_num in range(len(array) - 1, 0, - 1):
        # iterating through the list
        for i in range(pass_num):
            # checking if the array index that is currently being compared with the index beside is greater or not
            if array[i] > array[i + 1]:
                # switch process
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


# testing
array = [54, 34, 54, 654, 86, 967, 243, 63, 233]
bubble_sort(array)
print(array)


def short_bsort(arr):
    exchanges = True
    pass_num = len(arr) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                exchanges = True
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        pass_num -= 1


arr = [5454654, 34787, 567864, 687854, 88989876, 967867667, 24355656, 6376876, 28000]
bubble_sort(arr)
print(arr)
