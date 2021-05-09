import easygui
hello_text = easygui.msgbox("Эта программа преобразует градусы Фаренгейта в градусы Цельсия")
fahrengeit_degree = float(easygui.enterbox("Введите температуру в градусах Фаренгейта:"))
celsius_degree = (fahrengeit_degree - 32) * 5.0 / 9
result_text = easygui.msgbox("Результат в градусах Цельсия: " + str(celsius_degree) + " градуса")
print(result_text)
