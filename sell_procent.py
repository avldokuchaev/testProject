# В магазине распродажа. На товары за 10 долларов и меньше скидка 10%, а на товары дороже 10 долларов
# — 20 %. Напишите программу, которая будет запрашивать цену товара и показывать
# размер скидки (10 или 20 %) и итоговую цену.
cost_of_thing = float(input("Введите цену товара: "))
if cost_of_thing <= 10:

    cost_of_thing_with_saler = cost_of_thing - cost_of_thing * 0.1
    cost_of_thing_salers = cost_of_thing * 0.1
    print("Ваша скидка равна: 10%")
    print("Ваша скидка равна: ", round(cost_of_thing_salers, 1))
    print("Цена вашего товара: ", cost_of_thing_with_saler)
else:
    cost_of_thing_with_saler = cost_of_thing - cost_of_thing * 0.2
    cost_of_thing_salers = cost_of_thing * 0.2
    print("Ваша скидка равна: 20%")
    print("Ваша скидка равна: ", round(cost_of_thing_salers, 1))
    print("Цена вашего товара: ", cost_of_thing_with_saler)
