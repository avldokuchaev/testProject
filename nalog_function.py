def price_calc(price, tax_rate):
    total = price + (price * tax_rate)
    return total


my_price = float(input("Введите цену: "))
total_price = price_calc(my_price, 0.06)
print("Цена: ", total_price)
