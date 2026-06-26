class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}": "{", ")": "(", "]": "["}
        stack = deque()
        for bracket in s:
            if bracket in dic:
                print(bracket)
                stack.pop()
            else: stack.append(bracket)
        
        print(stack)

        return False if stack else True


