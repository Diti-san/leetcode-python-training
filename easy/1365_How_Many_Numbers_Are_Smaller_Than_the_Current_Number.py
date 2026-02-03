"""
Problem: 1365. How Many Numbers Are Smaller Than the Current Number
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
Difficulty: Easy
Topic: Mid Level, Array, Hash Table, Sorting, Counting Sort, Weekly Contest 178
Time Complexity: O(n + 100) ≈ O(n)
Space Complexity: O(1)
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101

        for x in nums:
            count[x] += 1

        for i in range(1, 101):
            count[i] += count[i - 1]

        res = []
        for x in nums:
            if x == 0:
                res.append(0)
            else:
                res.append(count[x - 1])

        return res
