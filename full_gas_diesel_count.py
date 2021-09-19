# Программа для рассчета количества литров топлива

# Формула для рассчета бензина

def benzine_count():
    print("Введите количество километров пути: ")
    full_km = float(input())
    print("Введите средний расход бензина на 100 км пути: ")
    gas_100 = float(input())
    print("Введите стоимость литра бензина: ")
    gas_tax = float(input())
    gas_all = full_km * gas_100 / 100
    gas_full_tax = gas_tax * gas_all
    print("Приблизительное количество бензина на весь путь = ", round(gas_all, 1))
    print("Приблизительная стоимость бензина на весь путь = ", round(gas_full_tax, 1))

# Формула для рассчета дизеля

def diesel_count():
    print("Введите количество километров пути: ")
    full_km_1 = float(input())
    print("Введите средний расход дизеля на 100 км пути: ")
    diesel_100_km = float(input())
    print("Введите стоимость литра дизеля: ")
    diesel_tax_l = float(input())
    diesel_all_l = full_km_1 * diesel_100_km / 100
    diesel_full_tax_l = diesel_tax_l * diesel_all_l
    print("Приблизительное количество бензина на весь путь = ", round(diesel_all_l, 1))
    print("Приблизительная стоимость бензина на весь путь = ", round(diesel_full_tax_l, 1))

# Формуля для сравнения бензина и дизеля

def benz_diesel_new():
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

# Вывод
benz_dies = int(input("""1. Для расчета бензина введите 1 
2. Для расчета дизеля введите 2
3. Для сравнения введите 3\n """))

if benz_dies == 1:
    benzine_count()
if benz_dies == 2:
    diesel_count()
if benz_dies == 3:
    benz_diesel_new()
