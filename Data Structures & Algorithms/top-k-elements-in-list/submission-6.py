class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        l = [[] for i in range(len(nums) + 1)]

        for num, c in count.items():
            l[c].append(num)
            
        res = []

        for i in range(len(l) - 1, 0, -1):
            for num in l[i]:
                res.append(num)
                if len(res) == k:
                    return res