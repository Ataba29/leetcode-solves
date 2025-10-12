from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"slow: {slow}, fast: {fast}")

            if slow == fast:
                break

        # Phase 2: Find entrance to cycle
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print(f"slow: {slow}, fast: {fast}")

        return slow


sol = Solution()

print(sol.findDuplicate([1, 3, 4, 2, 2]))
