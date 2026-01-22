"""
Problem: 8. String to Integer (atoi)
Link: https://leetcode.com/problems/string-to-integer-atoi
Difficulty: Medium
Topic: String
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Check overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
