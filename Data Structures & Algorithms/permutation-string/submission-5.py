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
        print(freq)
        
        check_freq = [0]*26
        for c2 in range(len(s1)):
                check_freq[ord(s2[c2]) - ord('a')] += 1
        print(check_freq)
        if check_freq == freq:
            return True

        for r in range(len(s1), len(s2)):
            check_freq[ord(s2[l])- ord('a')] -= 1
            check_freq[ord(s2[r]) - ord('a')] += 1
            print(check_freq)
            if check_freq == freq:
                return True
            else:
                l+=1
            
        
            
        return False


