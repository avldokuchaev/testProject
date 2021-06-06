import datetime
print(datetime.datetime.now()) # Текущая дата полная с временем
print(datetime.datetime.now().date()) # Текущий день с годом и месяцем
print(datetime.datetime.now().day) # Текущее число без месяца и года
print(datetime.datetime.now().month) # Текущий месяц без года и дня
print(datetime.datetime.now().year) # Текущий год
print(datetime.datetime.now().hour) # Текущий час без минут и секунд
print(datetime.datetime.now().minute) # Текущие минуты
print(datetime.datetime.now().second) # Текущие секунды