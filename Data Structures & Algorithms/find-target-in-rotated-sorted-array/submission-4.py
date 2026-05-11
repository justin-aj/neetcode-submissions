class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        i = 0
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            
            print(nums[l], nums[m], nums[r])
            if nums[l] <= nums[m]:
                if nums[l] >  target or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if nums[m] >  target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
