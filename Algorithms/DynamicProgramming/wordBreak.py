"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Ex. if input is "kingkong" and given words = ["king","kong"]
Return true because "kingkong" can be broken up as "king kong".
"""

# Brute force method is to recursively call wordBreak after breaking up the string and on remaining string. 
#       The recurrence relation to this is - T(n) = T(n-1) + T(n-2) + T(n-3) + ... + T(1) + O(cost of substring) = O(2^n) [think sum of powers of 2]
# Using memoization the relation becomes T(n) = T(n-1) which is N^2 [N recursive calls each of cost N]
# Time Complexity: O(n^2) - n is length of string
# Space Complexity: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        wordsSet = {word for word in wordDict}
        def helper(s):
            if not s:
                return True
            i = 0
            isWord = False
            while i < len(s):
                if s[:i + 1] in wordsSet:
                    if s[i + 1:] not in memo:
                        memo[s[i + 1:]] = helper(s[i + 1:])
                    isWord = isWord or memo[s[i + 1:]]
                i += 1
            memo[s] = isWord
            return memo[s]
        return helper(s)