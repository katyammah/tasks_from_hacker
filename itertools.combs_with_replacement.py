from itertools import combinations_with_replacement as cwr

S, k = map(str, input().split())
k = int(k)

combs = cwr(sorted(S), k)
for i in combs:
    print(''.join(i), end='\n')
