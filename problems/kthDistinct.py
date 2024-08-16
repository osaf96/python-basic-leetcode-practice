class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency = {}
    
        for item in arr:
            lower_item = item.lower()
            if lower_item in frequency:
                frequency[lower_item] += 1
            else:
                frequency[lower_item] = 1

        distinct_count = 0

        for item in arr:
            lower_item = item.lower()
            if frequency[lower_item] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return item  
        
        return ""
        