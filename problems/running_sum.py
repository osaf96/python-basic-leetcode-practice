from typing import List

# Running sum of 1d array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

# Plan
# 1. Loop through the array starting from the second element
# 2. Add the current element to the previous element
# 3. Update the current element with the sum
# 4. Return the array

# Time complexity: O(n)
# Space complexity: O(1)
# where n is the length of the array


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

sum  = Solution().runningSum([1,2,3,4])
print(sum) # [1,3,6,10]
