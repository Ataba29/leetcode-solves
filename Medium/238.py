class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        left = 1
        for i in range(n):
            ans[i] = left
            left = left * nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * right
            right = right * nums[i]

        return ans
