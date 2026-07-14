# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

kords = ["eat","tea","tan","ate","nat","bat"]

class groupAna:

    def getKey(self, word):
        countChar = [0] * 26
        for ch in word:
            countChar[ord(ch)-ord('a')] += 1
        return tuple(countChar)


    def anagram(self, words):
        groups = {}
        for word in words:
            key = self.getKey(word)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]    
        return list(groups.values())

grp = groupAna()
print(grp.anagram(kords))       


# Notes
# This solution has TC of O(N*K) where N is the number of words and K is the maximum length of a word
# SC is O(n), and we also other solution which is to sort string jion them, use them as key but
# sorting will result in klogk which combines with input n, resultant in n * klogk(k is char count)
# Our solution uses Tuple why because it is immutable and can be used as a key in a dictionary.
