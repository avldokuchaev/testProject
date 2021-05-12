# Напишите программу, выводящую на экран таблицу умножения. Первым делом она должна
# спрашивать, для какого числа требуется вывести таблицу.
number_for_multipl = int(input("Введите число для таблицы умножения: "))
number_1_for_multiple = int(input("Введите число до какого множителя: "))
# for i in range(1, 11):
#     print(i, "* ", number_for_multipl, "=", number_for_multipl * i)
i = 0
while i < number_1_for_multiple:
    print(i, "* ", number_for_multipl, "=", number_for_multipl * i)
    i += 1

