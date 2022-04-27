n = int(input())  # количество элементов в сете
s = set(map(int, input().split()))  # элементы множества

N = int(input())  # количество команд, которые нужно выполнить
for i in range(N):
    cmnd = input().split()
    if cmnd[0] == 'pop':
        s.pop()
    elif cmnd[0] == 'discard':
        s.discard(int(cmnd[1]))
    elif cmnd[0] == 'remove':
        s.remove(int(cmnd[1]))
print(sum(s))
