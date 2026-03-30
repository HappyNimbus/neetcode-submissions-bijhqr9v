class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:

                curr = nums[i] + nums[j] + nums[k]

                if curr == 0:
        
                    currOutput = [nums[i], nums[j], nums[k]]
                    output.append(currOutput)
                    j+=1
                    
                    while nums[j] == nums[j - 1] and j < k:
                        j+=1
                elif curr > 0:
                    k -= 1
                else:
                    j += 1
            

        return output