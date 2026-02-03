"""
Problem: 28. Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
Difficulty: Easy
Topic: Two Pointers, String, String Matching
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
