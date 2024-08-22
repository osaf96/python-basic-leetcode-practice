class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:] 
        newNum = ''
        for i in range(0,len(binary)): 
            newNum = newNum + "0" if binary[i] == '1' else newNum + '1'
        comp = int(newNum,2)
        return comp