"""
Problem: 389. Find the Difference
Link: https://leetcode.com/problems/find-the-difference
Difficulty: Easy
Topic: Hash Table, String, Bit Manipulation, Sorting
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def findTheDifference(self, s, t):
        res = 0

        for ch in s:
            res ^= ord(ch)

        for ch in t:
            res ^= ord(ch)

        return chr(res)


