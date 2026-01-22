"""
Problem: 7. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer
Difficulty: Medium
Topic: Math
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # check overflow
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res
