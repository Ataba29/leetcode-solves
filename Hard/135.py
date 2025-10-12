from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: Initialize left and right arrays to 1
        l = [1] * n
        r = [1] * n

        # Step 2: Left → Right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                l[i] = l[i - 1] + 1

        # Step 3: Right → Left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r[i] = r[i + 1] + 1

        # Step 4: Take the max of left and right for each child
        total_candies = sum(max(l[i], r[i]) for i in range(n))
        return total_candies
