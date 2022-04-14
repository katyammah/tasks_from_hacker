n = int(input())
#  собрано n марок разных стран, страны могут повторяться
#  посчитать, сколько вообще стран в коллекции марок
countries = set()
for i in range(n):
    country = str(input())
    countries.add(country)
print(len(countries))
