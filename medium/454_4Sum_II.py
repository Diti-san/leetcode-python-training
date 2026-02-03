"""
Problem: 454. 4Sum II
Link: https://leetcode.com/problems/4sum-ii
Difficulty: Medium
Topic: Array, Hash Table
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = {}

        for a in nums1:
            for b in nums2:
                s = a + b
                count[s] = count.get(s, 0) + 1

        res = 0
        for c in nums3:
            for d in nums4:
                s = c + d
                if -s in count:
                    res += count[-s]

        return res


