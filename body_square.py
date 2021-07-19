# Рассчет площади поверхности тела
height = input("Введите рост в сантиметрах: ")
weight = input("Введите вес в килограммах: ")

def square_body_chemotherapy():
    try:
        height_float = float(height)
        weight_float = float(weight)
        square_body = 0.0167 * weight_float ** 0.5 * height_float ** 0.5
        square_body_result = round(square_body, 2)
        return (square_body_result)
    except:
        return ("Вы ввели не число!")

doksorubicin = 60
ciklophosphamid = 600
res = square_body_chemotherapy()
doksorubicin_doza = doksorubicin * res
ciklophosphamid_doza = ciklophosphamid * res
print("Площадь поверхности тела = " + str(square_body_chemotherapy()) + " квадратных метров")
print("Необходимая доза Доксорубицина = " + str(round(doksorubicin_doza, 0)) + " мг")
print("Необходимая доза Циклофосфамида = " + str(round(ciklophosphamid_doza, 0)) + " мг")

k= input("Нажмите крестик для выхода!")
