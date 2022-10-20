"""
Time Complexity - O(S) where S is the the total number of chars 
or O(k * n) where k is avg # of chars in word and n words
Space Complexity - O(1)

LCP - Longest Common Prefix
Method used for solving - LCP(S1 ... Sn) = LCP(LCP(LCP(S1,S2),S3), ... Sn)


Can also use a Trie. Same the time complexity and O(S) space.
After inserting all the words into the Trie we traverse
    1) Trie until a node that has more than 1 child, or
    2) A node is the end of a word.
"""
def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    for i in range(len(strs)):
        lenPrefix = len(strs[0])
        while strs[i][:lenPrefix] != prefix and prefix:
            lenPrefix -= 1
            prefix = prefix[:lenPrefix]
        if not prefix: return ""
    return prefix