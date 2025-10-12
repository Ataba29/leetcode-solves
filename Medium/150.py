from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == "+":
                stk.append(int(stk.pop()) + int(stk.pop()))
            elif token == "-":
                stk.append(-int(stk.pop()) + int(stk.pop()))
            elif token == "*":
                stk.append(int(stk.pop()) * int(stk.pop()))
            elif token == "/":
                stk.append(int((1 / int(stk.pop())) * int(stk.pop())))
            else:
                stk.append(token)

        return int(stk[0])


sol = Solution()

print(
    sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)
