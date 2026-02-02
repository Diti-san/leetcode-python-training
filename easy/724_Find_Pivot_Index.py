"""
Problem: 724. Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/
Difficulty: Easy
Topic: Array, Prefix Sum, Weekly Contest 58
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1
