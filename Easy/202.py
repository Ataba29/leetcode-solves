class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(x):
            res = 0
            while x > 0:
                res += (x % 10) ** 2
                x //= 10
            return res

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1
