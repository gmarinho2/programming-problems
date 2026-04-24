class Solution:
    def isValid(self, s: str) -> bool:
        def isPair(par1: str, par2:str)->bool:
            if par1 == "(" and par2 == ")":
                return True
            if par1 == "[" and par2 == "]":
                return True
            if par1 == "{" and par2 == "}":
                return True
            return False

        stack = []
        for char in s:
            stack.append(char)
            if len(stack) < 2:
                continue
            if isPair(stack[len(stack)-2], stack[len(stack)-1]):
                stack.pop()
                stack.pop()

        if len(stack) == 0:
            return True
        return False
            