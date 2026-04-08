class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        string_set = set()
        l = 0

        for r in range(len(s)):
            
            while s[r] in string_set:

                string_set.remove(s[l])
                l += 1
            
            string_set.add(s[r])
            max_len = max(max_len, len(string_set))
        return max_len
                