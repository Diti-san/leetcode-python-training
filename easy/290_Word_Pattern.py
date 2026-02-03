"""
Problem: 290. Word Pattern
Link: https://leetcode.com/problems/word-pattern/
Difficulty: Easy
Topic: Hash Table, String
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for p, w in zip(pattern, words):
            if p in p_to_w:
                if p_to_w[p] != w:
                    return False
            else:
                if w in w_to_p:
                    return False
                p_to_w[p] = w
                w_to_p[w] = p

        return True

