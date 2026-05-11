class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = intervals[0]
        overlapping = 0

        for l, r in intervals[1:]:
            if last[1] > l:
                overlapping += 1
                last[1] = min(last[1], r)
            else:
                last[1] = r

        
        return overlapping