if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    d = {}
    for (name, score) in zip(names, scores):
        d[name] = score
    second = (sorted(list(set(d.values()))))[1]
    # нахожу у участников второй результат с конца по баллам

    out_list = []
    for name in d:
        if d[name]==second:
            out_list.append(name)
    # создаю список имён с найденным результатом

    out_str = '\n'.join(sorted(out_list))
    # преобразование отсортированного по алфавиту списка в строку

    print(out_str)

