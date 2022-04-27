from collections import Counter

shoes = int(input())  # кол-во пар обуви
sizes = map(int, input().split())  # размеры этих пар
customers = int(input())  # кол-во покупателей
s = Counter(sizes)

earned = 0
for i in range(customers):
    size, price = map(int, input().split())  # нужный покупателю размер и сумма, которую готов заплатить
    if s[size]:
        earned += price
        s[size] -= 1

print(earned)
