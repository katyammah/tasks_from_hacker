if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())  #  сумма всех чисел (x,y,z) в скобках не должна быть больше n

    a = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    a.append([i, j, k])
    print(a)
