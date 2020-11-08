# iterates through  a list while taking the smallest number and putting it into the start and shifts to the next index
# algorithm that uses the first index as a max value and uses a for loop to iterate through the array while comparing
# the max value. If the max value is less than the current index it stays the same


def selection_sort(arr):
    # had - 1 , 0, -1 to allow python to use selective functions (helps with multitask)
    for fillslot in range(len(arr) - 1, 0, -1):
        # setting a default max int as the beginning int
        maxpos = 0
        # iterating through the list
        for location in range(1, fillslot + 1):
            # checking if the location of our array rn compared to our max value, if the location is greater they swap
            if arr[location] > arr[maxpos]:
                # swapping phase
                maxpos = location

        # recursion
        temp = arr[fillslot]
        arr[fillslot] = arr[maxpos]
        arr[maxpos] = temp


arr = [14, 46, 43, 27, 57, 41, 45, 21, 70, 34934, 3434, 12, 323, 43, 12]
selection_sort(arr)
print(arr)

