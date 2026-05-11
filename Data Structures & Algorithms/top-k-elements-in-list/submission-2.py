class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        return heapq.nlargest(k, a.keys(), key=a.get)

