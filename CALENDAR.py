#  в задании нужно вывести день недели введённой даты
import datetime

DD, MM, YYYY = map(int, input('Введите дату (день, месяц, год): ').split(','))
print(datetime.datetime(YYYY, MM, DD).strftime('%A'))
