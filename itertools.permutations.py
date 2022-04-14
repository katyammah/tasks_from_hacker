from itertools import permutations

S, k = map(str, input().split())  # S - строка из заглавных букв, k - число
k = int(k)
# И снова вопрос по поводу ввода: в одну строчку ввод смогла записать, но мне кажется,
# как-то по-другому можно сделать?) без преобразования потом 'k' в 'int'
l1 = list(S)
l2 = sorted((permutations(l1, k)))
for i in l2:
    print(''.join(i), end='\n')
