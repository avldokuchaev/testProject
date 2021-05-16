import time
initial_time = int(input("Сколько секунд обратног отчета? "))
for i in range(initial_time, 0, -1):
    print(i)
    time.sleep(1)
print("Пуск!")