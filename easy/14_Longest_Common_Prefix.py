"""
Problem: 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/description/
Difficulty: Easy
Topic: Array, String, Trie
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        s1 = min(strs)
        s2 = max(strs)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]

        return s1

        
