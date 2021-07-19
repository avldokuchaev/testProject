# Рассчет площади поверхности тела
import easygui

def square_body_chemotherapy():
    height = easygui.enterbox("Введите рост в сантиметрах: ")
    weight = easygui.enterbox("Введите вес в килограммах: ")
    try:
        height_float = float(height)
        weight_float = float(weight)
        square_body = 0.0167 * weight_float ** 0.5 * height_float ** 0.5
        square_body_result = round(square_body, 2)
        return (square_body_result)
    except:
        return ("Вы ввели не число!")

print(easygui.msgbox("Площадь поверхности тела = " + str(square_body_chemotherapy()) + " кубических метров"))

