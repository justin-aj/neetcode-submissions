class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval[0], newInterval[1]
        res = []
        for l, r in intervals:
            if r < left:
                res.append([l, r])
            elif right < l:
                res.append([left, right])
                left = l
                right = r
            else:
                left = min(left, l)
                right = max(right, r)
            
        
        res.append([left, right])
        return res

            


