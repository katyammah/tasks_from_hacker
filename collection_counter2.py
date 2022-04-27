from collections import Counter

word = str(input())
a = Counter(sorted(word))
k = sorted(a.keys())
v = a.values()

for (x, y) in zip(k, v):
    print(x + str(y), end='')
