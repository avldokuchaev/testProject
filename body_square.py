# Рассчет площади поверхности тела

height = float(input("Введите рост в сантиметрах: "))
weight = float(input("Введите вес в килограммах: "))
square_body = 0.0167 * weight ** 0.5 * height ** 0.5
print(round(square_body, 2))
