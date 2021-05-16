import time
initial_time = int(input("Сколько секунд обратног отчета? "))
for i in range(initial_time, 0, -1):
    print(i, end=" ")
    for star in range(0, i):
        print("*", end=" ")
    print()
    time.sleep(1)
print("Пуск!")

