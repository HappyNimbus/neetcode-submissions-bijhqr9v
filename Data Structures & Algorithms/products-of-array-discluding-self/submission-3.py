class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #use prefix and suffix and 2 passes of the array
        output = []
        #[1,2,4,6]

        for i in range(len(nums)):
            value = 1
            for j in range(len(nums)):
                
                if j == i:
                    continue
                
                value *= nums[j]

            output.append(value)
        return output