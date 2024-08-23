from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        if left == right:
            return right * min(height[left], height[right])
        while left != right:
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_width * current_height
            if current_area > area:
                area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area