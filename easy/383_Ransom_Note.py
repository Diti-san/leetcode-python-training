"""
Problem: 383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Difficulty: Easy
Topic: Array, Greedy
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26

        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            idx = ord(c) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True
