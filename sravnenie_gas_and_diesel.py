print("Программа расчитывает количество литров топлива на весь путь и его стоимость. Сравнение бензина и дизеля.")
print("Введите количество километров пути: ")
full_km = float(input())
print("Введите средний расход топлива (бензин) на 100 км пути: ")
gas_100 = float(input())
print("Введите средний расход топлива (дизель) на 100 км пути: ")
disel_100 = float(input())
print("Введите стоимость литра бензина: ")
gas_tax = float(input())
print("Введите стоимость литра дизеля: ")
diesel_tax = float(input())
gas_all_benz = full_km * gas_100 / 100
diesel_all_full = full_km * disel_100 / 100
diesel_full_tax = diesel_tax * diesel_all_full
gas_full_tax = gas_tax * gas_all_benz
print("Приблизительное количество бензина на весь путь = ", round(gas_all_benz, 1))
print("Приблизительная стоимость бензина на весь путь = ", round(gas_full_tax, 1))
print("Приблизительное количество дизеля на весь путь = ", round(diesel_all_full, 1))
print("Приблизительная стоимость дизеля на весь путь = ", round(diesel_full_tax, 1))
