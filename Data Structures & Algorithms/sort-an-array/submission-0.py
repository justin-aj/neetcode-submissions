class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_sort = self.sortArray(nums[:mid])
        right_sort = self.sortArray(nums[mid:])
        return self.merge(left_sort, right_sort)

    def merge(self, L, R):
        x, y = 0, 0
        result = []

        while x < len(L) and y < len(R):
            if L[x] <= R[y]:
                result.append(L[x])
                x += 1
            else:
                result.append(R[y])
                y += 1
            
        result.extend(L[x:])
        result.extend(R[y:])
        return result
