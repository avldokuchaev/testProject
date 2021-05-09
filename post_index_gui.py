import easygui
# Программа запрашивает индекс, страну, город, улицу, номер дома, номер квартиры и имя.
# И выводит в виде окна
index_number = easygui.enterbox("Введите ваш индекс", default="213405")
print(index_number)
country_text = easygui.enterbox("Введите вашу страну", default="Россия")
print(country_text)
city_text = easygui.enterbox("Введите ваш город", default="Москва")
print(city_text)
street_text = easygui.enterbox("Введите вашу улицу", default="Михайловская")
print(street_text)
house_number = easygui.enterbox("Введите номер дома", default="д. 24")
print(house_number)
flat_number = easygui.enterbox("Введите номер квартиры", default="кв. 34")
print(flat_number)
your_name = easygui.enterbox("Введите ваше имя", default="Андрей Докучаев")
print(your_name)
result_message = easygui.msgbox(index_number + " " + country_text + " " + city_text + "\n"
                                + street_text + " " + house_number + ", " + flat_number + "\n"
                                + your_name)
print(result_message)
