class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position, speed), reverse=True)

        print(pairs)
        stack = deque()

        for pos, speed in pairs:
            time = ( target - pos ) / speed
            ## If current time is greater than stack
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)

