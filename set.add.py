n = int(input())
#  собрано n марок разных стран, страны могут повторяться
#  посчитать, сколько вообще стран в коллекции марок

countries = set(str(input()) for i in range(n))
print(len(countries))
