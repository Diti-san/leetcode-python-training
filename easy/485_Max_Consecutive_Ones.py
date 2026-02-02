"""
Problem: 485. Max Consecutive Ones
Link: https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                if current > max_count:
                    max_count = current
            else:
                current = 0

        return max_count
