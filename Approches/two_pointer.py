# Two pointer technique
# Use two different pointer to solve the problem invlolving indices with the
# benefits of saving time and space
# What are pointers?
# In computer science, a pointer is a reference to an object, In many programming
# languages, that object stores a memory address of another value locatied in computer 
# memory, or in some cases, that memeory-mapped computer hardware.

def has_pair_with_sum(nums, target):
    left = 0  # Start pointer
    right = len(nums) - 1  # End pointer

    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1  # Move left pointer to the right to increase the sum
        else:
            right -= 1  # Move right pointer to the left to decrease the sum
    
    return False  # No such pair found

nums = [1, 2, 3, 4, 6, 8, 9]
target = 10

result = has_pair_with_sum(nums, target)
print(result)  # Output: True, because 1 + 9 = 10 or 2 + 8 = 10
