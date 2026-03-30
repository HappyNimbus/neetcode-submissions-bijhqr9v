class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        arr = set(nums)
        longest = 0
        curr = 0

        if len(nums) == 1:
            return 1

        # -1,-1,0,1,3,4,5,6,7,8,9
        #   arr: 2,20,4,10,3
        #   curr: 1, longest: 1

        for n in arr:
            while n + curr in arr:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1

        return longest

