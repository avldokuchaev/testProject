print("Эта программа считает процент от числа.")
print("Введите общее количество: ")
full_count = float(input())
print("Введите другое количество: ")
next_count = float(input())
result_count = next_count * 100 / full_count
print("Искомый процент = ", round(result_count, 1))
