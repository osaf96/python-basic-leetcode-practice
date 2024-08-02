class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        
        if k == 0:
            return 0  
            
        current_ones = 0
        max_ones = 0

        
        for i in range(k):
            current_ones += nums[i]

        max_ones = current_ones

        for i in range(k, n + k):
            current_ones += nums[i % n] - nums[(i - k) % n]
            max_ones = max(max_ones, current_ones)

        return k - max_ones
            