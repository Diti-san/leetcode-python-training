"""
Problem: 242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Topic: Hash Table, String, Sorting
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            idx = ord(c) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False

        return True
