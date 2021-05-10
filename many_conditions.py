age = int(input("Сколько вам лет? "))
grade = int(input("В каком кассе вы учитесь? "))
if age >= 8:
    if grade >= 3:
        print("Вы можете играть в игру")
else:
    print("Вы слишком молоды!")