"""
Problem: 455. Assign Cookies
Link: https://leetcode.com/problems/assign-cookies
Difficulty: Easy
Topic: Array, Two Pointers, Greedy, Sorting
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0  # child index
        j = 0  # cookie index
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count



