class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        longest = 0
        curr = 0

        if len(nums) == 1:
            return 1

        # -1,-1,0,1,3,4,5,6,7,8,9

        for i in range(len(nums)):
            
            if i == 0:
                curr += 1
                longest = max(longest, curr)
                continue

            if nums[i - 1] == nums[i]:
                continue

            if nums[i] != nums[i - 1] + 1:
                curr = 1
            
            else:
                curr += 1
                longest = max(longest, curr)
        
        return longest

