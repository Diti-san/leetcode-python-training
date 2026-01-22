"""
Problem: 5. Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring
Difficulty: Medium
Topic: Two Pointers, String, Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, end = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # palindrome lẻ
            l1, r1 = expand(i, i)
            # palindrome chẵn
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

        
