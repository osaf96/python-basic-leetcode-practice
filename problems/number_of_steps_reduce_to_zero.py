# number of steps to reduce a number to zero
class Solution:
    def number_of_steps(self, num:int) -> int:
        steps = 0
        for i  in range(max(num, 1)):
            steps += 1  
            if num % 2 == 0:
                num = num // 2 
            else:
                num -=  1
            if num == 0:
                break 
        return steps
print(Solution().number_of_steps(14)) # 6