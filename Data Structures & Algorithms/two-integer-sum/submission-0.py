class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hMap = {}
        #3 : 4
        #4 : 3
        #5 : 2
        #6 : 1

        for i,v in enumerate(nums):
            compliment = target - nums[i]

            if compliment in hMap:
                return [hMap[compliment], i]
            
            hMap[v] = i
    