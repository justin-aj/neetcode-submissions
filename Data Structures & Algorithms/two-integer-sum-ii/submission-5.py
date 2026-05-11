class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = []
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in numbers and t != numbers[i]:
                f.append(i + 1)
        return f