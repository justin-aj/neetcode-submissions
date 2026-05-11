class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracket = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in bracket.values():
                stack.append(c)
            elif c in bracket:
                if not stack or stack.pop() != bracket[c]:
                    return False
            else:
                return False
        
        return not stack
