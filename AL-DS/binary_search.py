# Binary search algorithm
# Time complexity: O(log n)
# Space complexity: O(1)

# implementation of binary search algorithm

def binary_search(arr, x): # x is target element
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2 # Find mid element
 
        # If x is greater, ignore left half
        if arr[mid] < x:    
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return True
 
    # If we reach here, then the element was not present
    return False

print(binary_search([1,2,3,4,5,6,7,8,9], 5)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 10)) # False
print(binary_search([1,2,3,4,5,6,7,8,9], 1)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 9)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 8)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 7)) # True


