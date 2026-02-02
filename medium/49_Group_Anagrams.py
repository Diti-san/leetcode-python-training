"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topic: Array, Hash Table, String, Sorting
Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())
