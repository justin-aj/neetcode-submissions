from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            n = nums.copy()
            n.remove(i) 
            print(n)
            res = reduce(mul, n)
            output.append(res)
        
        return output