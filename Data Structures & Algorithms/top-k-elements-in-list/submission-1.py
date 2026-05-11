class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        print(a.items())
        b = dict(sorted(a.items(), key= lambda a: a[1], reverse=True))
        return list(b.keys())[:k]

