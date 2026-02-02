"""
Problem: 10. Regular Expression Matching
Link: https://leetcode.com/problems/regular-expression-matching
Difficulty: hard
Topic: String, Dynamic Programming, Recursion
Time Complexity: O(n)
Space Complexity: O(n)
""" 

class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        # Xử lý pattern dạng a*, a*b*, ...
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # '*' = 0 lần
                    dp[i][j] = dp[i][j - 2]

                    # '*' = >= 1 lần
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
