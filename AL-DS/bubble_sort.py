# Definition of bubble sort algorithm
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
# The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list.
# Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. It can be practical if the input is in mostly sorted 
# order with some out-of-order elements nearly in position.


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr)) # [11, 12, 22, 25, 34, 64, 90]
arr = [1,2,3,4,5,6,7,8,9]
print(bubble_sort(arr)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [9,8,7,6,5,4,3,2,1]
print(bubble_sort(arr)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
