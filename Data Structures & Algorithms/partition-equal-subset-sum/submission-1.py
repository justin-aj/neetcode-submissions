class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        """while r < len(nums):
            if l != r:
                # print(l, r)
                pass
            
            r += 1
            if r == len(nums):
                l += 1
                r = 0

            if l == len(nums):
                # return 
                pass"""
        
        a = set({0})

        t = sum(nums) // 2
        for i in range(len(nums)):
            nexta = a.copy()
            for j in a:
                total = j + nums[i]
                nexta.add(total)
            a = nexta

        print(t, a)
        return True if t in a else False