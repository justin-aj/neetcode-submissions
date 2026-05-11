class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        self.k = k
        self.nums = nums

        for num in self.nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)

        return self.hp[0]

        
