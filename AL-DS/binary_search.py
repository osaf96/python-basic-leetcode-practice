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




def binary_search_recursive(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2 
      
        # If element is present at the middle itself
        if arr[mid] == x:
            return True
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return False


print(binary_search([1,2,3,4,5,6,7,8,9], 5)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 10)) # False
print(binary_search([1,2,3,4,5,6,7,8,9], 1)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 9)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 8)) # True
print(binary_search([1,2,3,4,5,6,7,8,9], 7)) # True


print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 0, 8, 5)) # True
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 0, 8, 10)) # False
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 0, 8, 1)) # True
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 0, 8, 9)) # True
print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 0, 8, 8)) # True
 



