class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for tok in tokens:
            stack.append(tok)
            operator = ""
            if tok == "+" or tok == "-" or tok == "*" or tok == "/":
                operator = stack[-1]
                stack.pop(-1)
                second = int(stack[-1])
                stack.pop(-1)
                first = int(stack[-1])
                stack.pop(-1)
            if operator == "+":
                stack.append(first+second)
            if operator == "-":
                stack.append(first-second)
            if operator == "*":
                stack.append(first*second)
            if operator == "/":
                stack.append(first/second)

        return int(stack[-1])
            