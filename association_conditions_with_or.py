age = int(input("Сколько вам лет? "))
grade = int(input("В каком кассе вы учитесь? "))
favorite_color = input("Какой ваш любимый цвет? ")
if age >= 8 or grade >= 3 or favorite_color == "Фиолетовый":
    print("Вам можно играть в игру")
else:
    print("Вы не подходите для игры!")
