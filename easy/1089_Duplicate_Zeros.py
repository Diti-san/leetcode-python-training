"""
Problem: 1089. Duplicate Zeros
Link: https://leetcode.com/problems/duplicate-zeros
Difficulty: Easy
Topic: Senior, Array, Two Pointers, Weekly Contest 141
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        tmp = []

        for x in arr:
            tmp.append(x)
            if x == 0:
                tmp.append(0)

        for i in range(n):
            arr[i] = tmp[i]

