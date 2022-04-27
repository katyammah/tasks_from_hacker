from itertools import combinations
#  нужно составить все возможные комбинации (до k символов в комбинации)
#  из строки S.
S, k = map(str, input().split())

k = int(k)
S = sorted(list(S))
comb = combinations(S, k)

for i in range(k):
    comb = list(combinations(S, i + 1))
    i += 1
    for a in comb:
        print(''.join(a), end='\n')
