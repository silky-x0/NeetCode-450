# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number
# of instances that can be formed.

# Input: text = "loonbalxballpoon"
# Output: 2

text = "loonbalxballpoon"

fmap = {'b':0, 'a':0, 'l':0, 'o': 0, 'n': 0}

for s in text:
    if s in fmap:
        fmap[s]+=1

fmap['l']//=2                       
fmap['o']//=2 

print(min(fmap.values()))

# Notes and Explanation

# since we need to find instances of balloon we'll only track word "b", "a", "l", "o", "n"
# rest we have to ignore it and we need two of "l" and "o" we'll devide them 2 two in last
# and return minimum of all frequency of all chat count.