class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seen:
                return [seen[remain], i]
            seen[nums[i]] = i
