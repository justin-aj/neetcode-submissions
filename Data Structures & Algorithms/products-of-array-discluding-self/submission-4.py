class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        post = 1
        prefix = 1
        res = [1] * len(nums)

        for i, n in enumerate(nums):
            res[i] = post
            post = post * n
        
        print(res)
                
        for i in range(len(nums) - 1, -1, -1):
            res[i] = prefix * res[i]
            prefix = prefix * nums[i]


        return res
            

                