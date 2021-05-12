# Напишите программу, выводящую на экран таблицу умножения. Первым делом она должна
# спрашивать, для какого числа требуется вывести таблицу.
number_for_multipl = int(input("Введите число для таблицы умножения: "))
# for i in range(1, 11):
#     print(i, "* ", number_for_multipl, "=", number_for_multipl * i)
i = 0
while i < 10:
    i += 1
    print(i, "* ", number_for_multipl, "=", number_for_multipl * i)

