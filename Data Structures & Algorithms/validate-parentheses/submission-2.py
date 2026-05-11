class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for i in list(s):
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()  # Important thing here
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False