class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxFreq = 0
        maxOutput = 0

        curr = defaultdict(int)

        l = 0

        for r in range(len(s)):

            curr[s[r]] += 1
            maxFreq = max(maxFreq, curr[s[r]])

            while (r - l + 1) - maxFreq > k:
                curr[s[l]] -= 1
                l+=1
            
            maxOutput = max(maxOutput, (r - l + 1))
        
        return maxOutput
