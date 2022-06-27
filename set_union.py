def union():
    eng = int(input())  # число студентов с англ.подпиской
    set1 = set(input('enter ' + str(eng) + ' student names: ').split())
    if len(set1) != eng:
        print('you enter wrong number of students! start again:')
        union()




    french = int(input())  # число студентов с франц.подпиской
    set2 = set(input('enter ' + str(french) + ' student names: ').split()) # их номера (имена)
    if len(set1) != eng:
        print('you enter wrong number of students!')
        union()


    print(len(set1.union(set2)))  # найти кол-во студентов всего

# как записать 2 и 5 строчки так, чтобы был смысл в 1ой и 4ой?
# чтобы ввод имён студентов ограничился их указанным количеством.

union()

