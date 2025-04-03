import random

# Создание списка из 10 случайных чисел
numbers = [random.randint(1, 100) for _ in range(10)]

# Вывод списка
print("Список чисел:", numbers)

# Нахождение максимального и минимального значений
max_num = max(numbers)
min_num = min(numbers)

print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")

# Вычисление суммы всех элементов списка
sum_numbers = sum(numbers)
print(f"Сумма всех чисел: {sum_numbers}")

# Сортировка списка
numbers.sort()
print("Отсортированный список:", numbers)
