class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_interval = intervals[0]
        results = [new_interval]

        for l, r in intervals[1:]:
            if l > results[-1][1]:
                results.append([l, r])
            else:
                results[-1][1] = max(results[-1][1], r)
        
        return results


            


            
