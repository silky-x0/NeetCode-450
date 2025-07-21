# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.
 
# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

# Constraints:
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

class TrieNode:
    def __init__(self):
        self.childs = {}
        self.endOfWord = False

class wordDict:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.childs:
                cur.childs[c] = TrieNode()
            cur = cur.childs[c]
        cur.endOfWord = True

    def search(self, word):
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.childs.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.childs:
                        return False
                    cur = cur.childs[c]
            return cur.endOfWord
        return dfs(0, self.root)

wdict = wordDict()
wdict.addWord("bad")                     
wdict.addWord("dad")                     
wdict.addWord("mad")
print(wdict.search("mad"))                  
print(wdict.search(".ad"))                  
print(wdict.search("b.."))


# Notes and Explanation

# this search method is little tricky, our idea is we'll use a depth-first search (DFS) approach to explore all possible paths in the Trie.
# When we encounter a dot '.', we will try all possible children nodes at that position.
# If we find a match, we return True. If we exhaust all possibilities without finding a match, we return False.
