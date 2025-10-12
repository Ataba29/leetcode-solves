from cmath import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, n

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            left1 = nums1[i - 1] if i > 0 else -inf
            right1 = nums1[i] if i < n else inf
            left2 = nums2[j - 1] if j > 0 else -inf
            right2 = nums2[j] if j < m else inf

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1

        return None
