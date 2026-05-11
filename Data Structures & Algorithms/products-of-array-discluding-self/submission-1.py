class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r  = 0, 0

        prods = 1
        total_prods = []
        while r < len(nums):
            if l != r:
                print(nums[l], prods, nums[r])
                prods = prods * nums[r]

            r += 1

            if r == len(nums):
                total_prods.append(prods)
                l += 1
                r = 0
                prods = 1
            
            if l == len(nums):
                break

        return total_prods           
