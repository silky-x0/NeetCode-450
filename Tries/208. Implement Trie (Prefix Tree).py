class TrieNode():
    def __init__(self):
        self.childrens = {}
        self.endOfWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            curr = curr.childrens[c]
        curr.endOfWord = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c in curr.childrens:
                curr = curr.childrens[c]
        return curr.endOfWord

    def startsWith(self, word):
        curr = self.root
        for c in word:
            if c not in curr.childrens:
                return False
            curr = curr.childrens[c]
        return True    

prefixTree = Trie()
prefixTree.insert("apple")
print(prefixTree.search("apple"))
print(prefixTree.startsWith("app"))                           
print(prefixTree.startsWith("apps"))                           