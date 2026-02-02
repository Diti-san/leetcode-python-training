"""
Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Topic: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
Time Complexity: O(n)
Space Complexity: O(n)
"""

import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
