class Solution:
    def sumAndMultiply(self, n: int) -> int:
        noZero = [int(c) for c in str(n) if c != "0"]
        x = int("".join(map(str, noZero))) if noZero else 0
        return x * sum(noZero)


print(Solution().sumAndMultiply(10203004))
