"""
Problem: 912. Sort an Array
Link: https://leetcode.com/problems/sort-an-array/
Difficulty: Easy
Topic: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])
        return res
