class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = [1] * len(nums)
        j = 0
        for i in range(len(nums)):
            while j < len(nums):
                if i != j:
                    nums1[i] = nums1[i] * nums[j]
                    print(nums1)           
                if j == len(nums) - 1: 
                    j = 0
                    break
                j += 1
        
        return nums1
                

            

                