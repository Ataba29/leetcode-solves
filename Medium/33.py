from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val == target:
                return mid
            if nums[l] <= val:
                if nums[l] <= target < val:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target > val:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


sol = Solution()
print(sol.search(nums=[3, 1], target=1))
