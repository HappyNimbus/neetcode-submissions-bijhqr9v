class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        output = set()
        curr = 0
        l = 0

        for r in range(len(s)):
            
            while s[r] in output:
                output.remove(s[l])
                l += 1
    
            output.add(s[r])

            curr = max(len(output), curr)
        
        return curr