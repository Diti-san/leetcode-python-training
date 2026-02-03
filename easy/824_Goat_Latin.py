"""
Problem: 824. Goat Latin
Link: https://leetcode.com/problems/goat-latin/
Difficulty: Easy
Topic: Senior, String, Weekly Contest 82
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def toGoatLatin(self, sentence):
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        res = []

        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"

            new_word += "a" * i
            res.append(new_word)

        return " ".join(res)



        
