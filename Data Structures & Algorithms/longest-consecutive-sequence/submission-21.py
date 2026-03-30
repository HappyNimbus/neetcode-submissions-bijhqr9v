class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        arr = set(nums)
        longest = 0
        curr = 0

        for n in arr:

            curr = 1

            while n + curr in arr:
                curr += 1
                longest = max(longest, curr)
            
            longest = max(longest, curr)
        
        return longest
            
