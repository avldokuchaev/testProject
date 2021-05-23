# Напишите функцию,которая будет выводить на экран имя,номера  квартиы и дома,
# названия улицы и города, почтовый индекс и название страны.
def func_address(name, post_index, country, town, street, house_number, room_number):
    print(name)
    print(post_index, end=" ")
    print(country, end=" ")
    print(town, end=" ")
    print(street, end=" ")
    print(house_number, end=" ")
    print(room_number)
    print()


func_address("Viktor", "215465", "Russia", "Moskow", "Nahimova", "34", "56")
