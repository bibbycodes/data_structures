# Leetcode 140
# Given a non-empty string s and a dictionary wordDict containing
# a list of non-empty words, add spaces in s to construct a sentence
# where each word is a valid dictionary word. Return all such possible sentences

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
string = "a"
wordDict = ["a"]

class Solution:
    def __init__(self):
            self.arr = []

    def wordBreak(self, string, wordDict):
        lengths = self.get_lengths(wordDict)
        wordDict = dict.fromkeys(wordDict, string)
        self.sol(0, string, lengths, wordDict)
        return self.arr
        
    def sol(self, start, string, lengths, wordDict, returned_string = "", cached = {}):
        if returned_string in cached:
            return cached[returned_string]
        cached[returned_string]

        if start > len(string) - 1:
            if returned_string not in self.arr:

                self.arr.append(returned_string)
                return

        for length in lengths:
            word = string[start : start + length]
            if word in wordDict:
                if start == 0:
                    self.sol(start + length, string, lengths, wordDict, returned_string + word)
                else:
                    self.sol(start + length, string, lengths, wordDict, returned_string + " " + word)
                    
    def get_lengths(self, arr):
        return set(map(lambda x : len(x), arr))

s = Solution()

s.wordBreak(string, wordDict)