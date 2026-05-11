import math
class MedianFinder:

    def __init__(self):
        self.num = 0
        self.li = []
        

    def addNum(self, num: int) -> None:
        self.num = num
        self.li.append(self.num)
        print(self.li)
        

    def findMedian(self) -> float:
        sorted_list = sorted(self.li)
        n = len(sorted_list)
        # Use floor division for index
        mid_index = n // 2

        if n % 2 == 1:
            # Odd length: the median is the middle element
            return sorted_list[mid_index]
        else:
            # Even length: the median is the average of the two middle elements
            return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
        
        