class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}": "{", ")": "(", "]": "["}
        stack = deque()
        for bracket in s:
            if bracket in dic:
                if stack[-1] == dic[bracket]:
                    print(bracket)
                    stack.pop()
                else:
                    return False
            else: stack.append(bracket)
    
        return False if stack else True


