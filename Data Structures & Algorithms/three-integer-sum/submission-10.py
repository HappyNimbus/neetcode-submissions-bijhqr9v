class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums.sort()

        #-4,-1,-1,0,1,2
        for i in range(len(nums)):
            j = 1 + i
            k = len(nums)-1

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:

                curr = nums[i] + nums[j] + nums[k]

                if curr == 0:
                    output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    
                elif curr < 0:
                    j+=1
                else:
                    k-=1
            
        return output

