# Программа запрашивает число n и выполняет вычисления с использованием цикла while.

# Ввод числа
n = int(input("Введите число n: "))

# Вывод чисел от n до 1
print("Числа от n до 1:")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

# Вычисление факториала числа n
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"Факториал числа {n}: {factorial}")
``
