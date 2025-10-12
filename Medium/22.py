from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, str):
            if open == close and open + close == 2 * n:
                res.append(str)
                return

            if open < n:
                dfs(open + 1, close, str + "(")
            if close < open:
                dfs(open, close + 1, str + ")")

        dfs(0, 0, "")
        return res


sol = Solution()
print(sol.generateParenthesis(2))
