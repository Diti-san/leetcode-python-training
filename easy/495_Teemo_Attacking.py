"""
Problem: 495. Teemo Attacking
Link: https://leetcode.com/problems/teemo-attacking
Difficulty: Easy
Topic: Array, Simulation
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries or duration == 0:
            return 0

        total = 0

        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i - 1])

        total += duration
        return total




