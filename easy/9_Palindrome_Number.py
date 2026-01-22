"""
Problem: 9. Palindrome Number
Link: hhttps://leetcode.com/problems/palindrome-number
Difficulty: Easy
Topic: String
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers or numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits:  x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

        
