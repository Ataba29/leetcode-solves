from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_idx = {}
        for idx, num in enumerate(nums):
            if num in last_idx and idx - last_idx[num] <= k:
                return True
            last_idx[num] = idx
        return False
