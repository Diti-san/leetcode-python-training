"""
Problem: 1. TwoSum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Array, Hash Table
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seen:
                return [seen[remain], i]
            seen[nums[i]] = i
