from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k

        while low < high:
            mid = (low + high) // 2

            # Compare which end is closer to x
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid

        # low is the start index of the closest window
        return arr[low : low + k]
