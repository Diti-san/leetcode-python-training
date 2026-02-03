"""
Problem: 771. Jewels and Stones
Link: https://leetcode.com/problems/jewels-and-stones
Difficulty: Easy
Topic: Hash Table, String, Weekly Contest 69
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        count = 0

        for c in stones:
            if c in jewel_set:
                count += 1

        return count



        
