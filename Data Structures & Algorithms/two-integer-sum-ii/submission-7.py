class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = defaultdict(int)
        for i in range(len(numbers)):
            t = target - numbers[i]
            if f[t]:
                return [f[t], i + 1]
            f[numbers[i]] = i + 1
            print(f)
        return f