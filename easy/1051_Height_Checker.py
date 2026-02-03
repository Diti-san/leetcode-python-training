"""
Problem: 1051. Height Checker
Link: https://leetcode.com/problems/height-checker
Difficulty: Easy
Topic: Junior, Array, Sorting, Counting Sort, Weekly Contest 138
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count
