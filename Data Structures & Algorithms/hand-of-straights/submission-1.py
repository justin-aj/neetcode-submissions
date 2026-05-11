from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Odd Count - return False
        if len(hand) % groupSize != 0:
            return False
        
        # Hashmap to get frequency
        hashmap = Counter(hand)
        heap = list(hashmap.keys())
        heapq.heapify(heap)
        
        # Start of heap
        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                # If i not in hashmap - return False
                if not hashmap[i]:
                    return False
                
                # Decrement - happens on True
                hashmap[i] -= 1

                # If freq is 0 for i then?
                if hashmap[i] == 0:

                    # If its not first element return False as it means there are gaps
                    if heap[0] != i:
                        return False

                    # Pop from heap as its count is 0
                    heapq.heappop(heap)
        
        return True