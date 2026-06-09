class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a/b),
        
        }
        stack = []

        for ch in tokens:
            if ch in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[ch](b,a))
            else:
                stack.append(int(ch))
        return stack[-1]
                

        