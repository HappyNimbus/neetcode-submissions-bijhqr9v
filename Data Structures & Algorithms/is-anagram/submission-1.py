class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        hMap = {}

        for c in s:
            hMap[c] = hMap.get(c , 0) + 1
        
        for c in t:
            
            if c not in hMap or hMap[c] == 0:
                return False
            
            hMap[c] -= 1
        return True
        