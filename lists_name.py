# Напишите программу,которая будет запрашивать у пользователя пять имен.
# Имена должны сохраняться в списке и выводиться в конце программы.
name_list = []
print("Введите пять имен")
name_list.append(input("Введите первое имя: "))
name_list.append(input("Введите второе имя: "))
name_list.append(input("Введите третье имя: "))
name_list.append(input("Введите четвертое имя: "))
name_list.append(input("Введите пятое имя: "))
print("Это имена: ", end=" ")
for names in name_list:
    print(names, end=" ")
print()
# name_list.sort()
# print("Эти имена отсортированы: ", end=" ")
# for names in name_list:
#     print(names, end=" ")
# print()
print("Третье введенное имя: ", name_list[2])
