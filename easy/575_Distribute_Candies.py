"""
Problem: 575. Distribute Candies
Link: https://leetcode.com/problems/distribute-candies
Difficulty: Easy
Topic: Array, Hash Table
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType)
        return min(len(set(candyType)), n >> 1)





