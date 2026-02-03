"""
Problem: 1304. Find N Unique Integers Sum up to Zero
Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
Difficulty: Easy
Topic: Mid Level, Array, Math, Weekly Contest 169
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def sumZero(self, n):
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)

        if n % 2 == 1:
            res.append(0)

        return res
