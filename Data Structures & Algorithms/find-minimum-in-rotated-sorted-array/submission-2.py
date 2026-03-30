class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        curMin = 0

        while l <= r:

            mid = (l + r)//2

            if nums[l] == nums[mid]:
                return min(nums[mid], nums[r])

            if nums[l] > nums[r]:

                if nums[l] > nums[mid]:
                    r = mid
                else:
                    l = mid
            
            else:
                r = mid


    