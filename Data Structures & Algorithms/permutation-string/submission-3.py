class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        
        if len(s1) > len(s2):
            return False
        
        l = 0

        freq = [0]*26
        
        for c1 in s1:
            freq[ord(c1) - ord('a')] += 1

        for r in range(len(s1)-1, len(s2)):
            check_freq = [0]*26

            for calc in range(l, r + 1):
                
                check_freq[ord(s2[calc]) - ord('a')] += 1
            
            if check_freq == freq:
                return True
            else:
                l+=1
            
        return False


