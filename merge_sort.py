# merge sort algorithm
# divide and conquer algorithm, once broken down, compares indexes and merges back into one array
# recursive function, calls itself to keep dividing itself till size becomes one


def merge_sort(arr): # this whole chunk breaks down the array 
    if len(arr) > 1:
        # finds the mid of the array
        mid = len(arr) // 2
        # break the list into 2 halves
        left = arr[:mid]
        right = arr[mid:]
        # calling itself to divide even further
        left = merge_sort(left)
        right = merge_sort(right)

        arr = []

        # copying data to temp arrays
        while len(left) > 0 and len(right) > 0:
            # checking if left index is smaller, if it is I want to remove from original array and place it as the
            # first thing on my new array
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)

            else:
                # if the right index was smaller
                arr.append(right[0])
                right.pop(0)

        # forming the array with a for loop by iterating it
        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)

    return arr


# Input list
a = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(*a)

a = merge_sort(a)

# Print output
print("Sorted array is : ")
print(*a)
