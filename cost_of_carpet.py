lenght_of_room = float(input("Введите длину комнаты в сантиметрах: "))
width_of_room = float(input("Введите ширину комнаты в сантиметрах: "))
cost_of_carpet_to_m = float(input("Введите стоимость ковра за квадратный метр: "))
square_of_carpet = lenght_of_room * width_of_room
square_of_carpet_m_2 = square_of_carpet / 10000
cost_of_carpet = cost_of_carpet_to_m * square_of_carpet_m_2
print("Для покрытия комнаты необходим ковер площадью", square_of_carpet, "см^2.")
print("Это", square_of_carpet_m_2, "м^2")
print("Стоимость ковра:", cost_of_carpet, "долларов.")
