class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -(2**31)  # -2147483648

        res = 0
        negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying/reserving
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0

            res = res * 10 + digit

        if negative:
            res = -res
        return res
