class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count = 0

        for num in nums:
            complement = k - num
            if count_map[complement] > 0:
                count += 1
                count_map[complement] -= 1  # Use up one occurrence of the complement
            else:
                count_map[num] += 1  # Store the current number for future pairs

        return count