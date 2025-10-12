from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            val = numbers[r] + numbers[l]

            if val == target:
                return [l + 1, r + 1]
            elif val > target:
                r -= 1
            else:
                l += 1
        return []
