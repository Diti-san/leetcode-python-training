"""
Problem: 58. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy
Topic: String
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])
