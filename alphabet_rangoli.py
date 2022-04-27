import string

letters = string.ascii_lowercase

def print_rangoli(size):
    width = n * 4 - 3
    rang = []
    for i in range(n):
        s = '-'.join(letters[i:n])  # строка в ранголи
        rang.append((s[::-1] + s[1:]).center(width, '-'))  # половина строк в ранголи
    RANG = rang[:0:-1] + rang  # все строки в ранголи
    print('\n'.join(RANG))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
