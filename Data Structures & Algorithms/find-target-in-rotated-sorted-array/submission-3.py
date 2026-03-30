class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        output = -1

        #6,7,1,2,3,4,5
        while l <= r:

            m = (l + r)//2

            if nums[l] == nums[m]:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                else:
                    return -1

            if nums[l] <= nums[m]:
                #left sorted
                if nums[m] >= target >= nums[l]:
                    r = m
                else:
                    l = m
                
            else:
                #right sorted
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m

        return output
            