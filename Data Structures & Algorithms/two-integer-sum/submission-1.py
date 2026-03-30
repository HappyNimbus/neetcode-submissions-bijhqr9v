class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hMap = {}
        #3 : 0
        #4 : 3
        #5 : 2
        #6 : 1

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in hMap:
                return [hMap[compliment], i]
            
            hMap[nums[i]] = i
    