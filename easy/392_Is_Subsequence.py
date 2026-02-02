"""
Problem: 392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/description/
Difficulty: Easy
Topic: Two Pointers, String, Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)
"""

import bisect

class Solution:
    def isSubsequence(self, s, t):
        pos = {}

        # Preprocess t
        for i, c in enumerate(t):
            if c not in pos:
                pos[c] = []
            pos[c].append(i)

        prev = -1
        for c in s:
            if c not in pos:
                return False

            idx_list = pos[c]
            j = bisect.bisect_right(idx_list, prev)
            if j == len(idx_list):
                return False

            prev = idx_list[j]

        return True

        
