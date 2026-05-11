class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = ["+", "-", "*", "/"]
        for tok in tokens:
            if tok in operators:
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                elif tok == "/":
                    stack.append(int(a/b))            
            else:
                stack.append(int(tok))
        
        return stack[0]
