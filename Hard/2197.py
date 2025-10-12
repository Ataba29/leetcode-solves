from typing import List


class Solution:
    def gcd(self, x, y):
        if x < y:
            return self.gcd(y, x)
        while y != 0:
            x, y = y, x % y
        return x

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            while stack:
                g = self.gcd(stack[-1], num)
                if g == 1:
                    break
                num = stack.pop() * num // g
            stack.append(num)

        return stack
