def insertion_sort(arr):
    # the range parameter is start,end, step
    # setting the start of the array to the first index
    # traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        # key is the index ahead of the key getting compared
        key = arr[i]
        # key getting compared (behind key)
        current_element = i - 1
        # if the key ahead of my current element is greater, switch places
        while current_element >= 0 and key < arr[current_element]:
            # switching the elements
            arr[current_element + 1] = arr[current_element]
            # shifting to the next key
            current_element -= 1
        arr[current_element + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
