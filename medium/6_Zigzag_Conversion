"""
Problem: 6. Zigzag Conversion
Link: https://leetcode.com/problems/zigzag-conversion
Difficulty: Medium
Topic: String
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row = 0
        direction = -1  # đổi hướng khi chạm biên

        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
            cur_row += direction

        return "".join(rows)
