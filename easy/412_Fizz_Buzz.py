"""
Problem: 412. Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz
Difficulty: Easy
Topic: Math, String, Simulation
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def fizzBuzz(self, n):
        return [
            "FizzBuzz" if i % 15 == 0 else
            "Fizz" if i % 3 == 0 else
            "Buzz" if i % 5 == 0 else
            str(i)
            for i in range(1, n + 1)
        ]


