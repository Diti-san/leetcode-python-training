"""
Problem: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topic: Array, Hash Table, Sorting
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
