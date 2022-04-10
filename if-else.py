if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')

# https://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html
# какие то мои исправления могу быть неверными, так как я не помню точно всех заданий, твое решение тоже отличино работает,
# но стоит избегать увелечения уровня вложенности
