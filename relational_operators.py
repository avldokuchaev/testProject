num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 < num2:
    print(num1, "меньше", num2)
elif num1 > num2:
    print(num1, "больше", num2)
elif num1 == num2:
    print(num1, "равно", num2)
elif num1 != num2:
    print(num1, "не равно", num2)
else:
    print("До свидания!")
