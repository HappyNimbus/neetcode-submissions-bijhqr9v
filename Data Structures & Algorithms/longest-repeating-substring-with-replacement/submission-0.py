class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxOutput = 0
        maxFreq = 0

        hMap = {}
        l = 0
        #[A,B,C,C,D,E,C] k = 2
        for r in range(len(s)):
            
            hMap[s[r]] = hMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hMap[s[r]])
            
            while (r - l + 1) - maxFreq > k:
                hMap[s[l]] -= 1
                l += 1
            maxOutput = max(maxOutput, r - l + 1)
        return maxOutput
