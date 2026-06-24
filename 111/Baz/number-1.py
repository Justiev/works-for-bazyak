import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


# Задаём функцию f(x)
# Исходное уравнение:
# 2^(-x) = sin(x)
# Переносим всё влево:
# 2^(-x) - sin(x) = 0
def f(x):
    return 2 ** (-x) - math.sin(x)


# Функция для поиска промежутков, где есть корни
def find_intervals(left, right, h):
    # Сюда будем сохранять найденные интервалы
    intervals = []

    # Начинаем проверку с левой границы
    x = left

    # Пока x меньше правой границы
    while x < right:
        a = x
        b = x + h

        # Если f(a) и f(b) имеют разные знаки,
        # значит между a и b есть корень
        if f(a) * f(b) < 0:
            intervals.append([a, b, f(a), f(b)])

        x += h

    # Возвращаем найденные интервалы
    return intervals

left = 0

# Правая граница поиска, по условию x < 10
right = 10

# Шаг поиска
h = 0.01

# Ищем интервалы, где находятся корни
intervals = find_intervals(left, right, h)

# Выводим найденные интервалы в красивой таблице
print("Отделённые интервалы корней:")
print(tabulate(
    intervals,
    headers=["a", "b", "f(a)", "f(b)"],
    tablefmt="grid",
    floatfmt=".6f"
))

# Создаём 1000 точек от 0 до 10 для графика
x_values = np.linspace(left, right, 1000)

# Для каждой точки x считаем значение функции f(x)
y_values = [f(x) for x in x_values]

# Строим график функции
plt.plot(x_values, y_values, label="f(x) = 2^(-x) - sin(x)")

# Рисуем горизонтальную линию y = 0
plt.axhline(0, color="black", linewidth=1)

plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции f(x)")
plt.legend()

plt.show()