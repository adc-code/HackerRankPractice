# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

N = int(input())

words = collections.OrderedDict ()
for item in range (N):
    word = input()
    #print (word)
    #@print (type(word))
    if (word in words.keys()):
        words[word] += 1
    else:
        words[word] = 1

print (len(words))

for k, v in words.items():
    print (v, end=" ")



