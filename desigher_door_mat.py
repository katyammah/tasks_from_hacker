height, width = map(int, input().split())
# высота должно быть не меньше 5
# ширина должна быть в 3 раза больше высоты

# верхний узор
for i in range((height-1)//2):
    print((('.|.' * i) + '.|.' + ('.|.' * i)).center(width, '-'))

# средняя линия
for i in range(1):
    print("WELCOME".center(width, '-'))

# нижний узор
for i in range((height-1)//2, 0, -1):
    print((('.|.' * (i-1)) + '.|.' + ('.|.' * (i-1))).center(width, '-'))
