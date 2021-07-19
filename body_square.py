# Рассчет площади поверхности тела
import easygui

def square_body_chemotherapy():
    height = float(easygui.enterbox("Введите рост в сантиметрах: "))
    weight = float(easygui.enterbox("Введите вес в килограммах: "))
    square_body = 0.0167 * weight ** 0.5 * height ** 0.5
    square_body_result = round(square_body, 2)
    return(square_body_result)

print(easygui.msgbox("Площадь поверхности тела = " + str(square_body_chemotherapy()) + " кубических метров"))

