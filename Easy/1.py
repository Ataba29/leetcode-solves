class Solution(object):
    def twoSum(self, nums, target):
        idx = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in idx:
                return [i, idx[comp]]
            idx[nums[i]] = i
        return []
