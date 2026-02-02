"""
Problem: 387. First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Difficulty: Easy
Topic: Hash Table, String, Queue, Counting
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def firstUniqChar(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1



