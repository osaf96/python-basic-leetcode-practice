class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            letterFound = magazine.find(ransomNote[i])
            if(letterFound == -1):
                return False
            else:
                magazine = magazine[:letterFound] + magazine[letterFound+1:] # Remove the letter from the magazine
        return True
            
print(Solution().canConstruct("aa", "aba")) # 

