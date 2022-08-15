"""
Given a string s, return the longest palindromic substring in s.

Explanation - Use dynamic programming to reduce the time complexity from N^3 to N^2. 
Instead of checking if each substring is a palindrome use the base cases - a letter, and two same letters. 
"""
# Time Complexity : O(N^2)
# Space Complexity : O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalStr = s[0]
        
        def findPalindrome(l, r):
            nonlocal longestPalStr
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                if (r - l + 1) > len(longestPalStr):
                    longestPalStr = s[l : r + 1]
                l -= 1
                r += 1
                    
        for i in range(len(s)):
            findPalindrome(i, i+1)
            findPalindrome(i-1, i+1)
        
        return longestPalStr