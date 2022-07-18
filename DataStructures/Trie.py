"""
Trie Data Structure (Prefix Tree)
Description - A trie or prefix tree is optimal for efficient insertions and lookups.
Especially, useful for prefix lookups. Often used in auto-complete and auto-correct.
Complexities - Let k be the avg chars in N words. Then, creation is O(k * N)
Lookup/Search is O(k)
Insertion is O(k)
Deletion is O(k)
Prefix lookup is O(prefixLength)

A hashmap might be better for insertions and lookups (given optimal hashing function). 
However, trie is great for prefix lookups
"""
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def get(self, c):
        return self.children[ord(c) - ord('a')]

    def set(self, c, val):
        self.children[ord(c) - ord('a')] = val
            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.get(c):
                cur.set(c, TrieNode())
            cur = cur.get(c)
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.get(c):
                return False
            cur = cur.get(c)
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.get(c):
                return False
            cur = cur.get(c)
        return True