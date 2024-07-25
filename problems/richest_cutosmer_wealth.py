#Example 1:
#    Input: accountes = [[1,2,3],[3,2,1]]
#    Output: 6
#    Explanation: The richest customer has wealth = 6
#Example 2:
#    Input: accountes = [[1,5],[7,3],[3,5]]
#    Output: 10
#    Explanation: The richest customer has wealth = 10


# Plan
# 1. Initialize a variable to store the maximum wealth
# 2. Loop through the accounts
# 3. Calculate the sum of each customer's wealth
# 4. Update the maximum wealth if the current customer's wealth is greater
# 5. Return the maximum wealth
# Time complexity: O(n*m)

# Solution

from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            wealth = sum(account)
            max_wealth = max(max_wealth, wealth)
        return max_wealth
print(Solution().maximumWealth([[1,2,3],[3,2,1]])) # 6
print(Solution().maximumWealth([[1,5],[7,3],[3,5]])) # 10
print(Solution().maximumWealth([[1,5],[7,3],[3,5],[1,1,1,1,1]])) # 10
print(Solution().maximumWealth([[1,5],[7,3],[3,5],[1,1,1,1,1],[
    1,5],[7,3],[3,5],[1,1,1,1,1]])) # 10

# Solution 2
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            wealth = 0
            for w in account:
                wealth += w
            if(max_wealth < wealth):
                max_wealth = wealth
        return max_wealth
    
print(Solution().maximumWealth([[1,2,3],[3,2,1]])) # 6
print(Solution().maximumWealth([[1,5],[7,3],[3,5]])) # 10
print(Solution().maximumWealth([[1,5],[7,3],[3,5],[1,1,1,1,1]])) # 10
print(Solution().maximumWealth([[1,5],[7,3],[3,5],[1,1,1,1,1],[
    1,5],[7,3],[3,5],[1,1,1,1,1]])) # 10


# Best Solution

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])
    
print(Solution().maximumWealth([[1,2,3],[3,2,1]])) # 6
print(Solution().maximumWealth([[1,5],[7,3],[3,5]])) # 10
print(Solution().maximumWealth([[1,5],[7,3],[3,5],[1,1,1,1,1]])) # 10         


 
        