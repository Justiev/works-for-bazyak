import math
from tabulate import tabulate


# f(x) = 0 означает, что корень найден
def f(x):
    return 2 ** (-x) - math.sin(x)



# Исходное уравнение:
# 2^(-x) = sin(x)
# x = arcsin(2^(-x))
def phi(x):
    return math.asin(2 ** (-x))


# Метод простой итерации
def simple_iteration(x0, eps):
    # Таблица для хранения шагов
    table = []

    # Номер итерации
    k = 0

    while True:
        # Считаем новое значение x по формуле:
        # x_(k+1) = phi(x_k)
        x_next = phi(x0)

        # Добавляем данные текущего шага в таблицу
        table.append([
            k,                       # номер итерации
            x0,                      # текущее значение x_k
            x_next,                  # новое значение x_(k+1)
            abs(x_next - x0),        # разница между новым и старым значением
            f(x_next)                # значение функции в новой точке
        ])

        if abs(x_next - x0) < eps:
            return x_next, table

        # Старое значение заменяем новым
        x0 = x_next

        # Увеличиваем номер итерации
        k += 1


# Начальное приближение для первого корня
x0 = 0.675

# Точность 10^-6
eps = 10 ** (-6)

# Запускаем метод простой итерации
root, table = simple_iteration(x0, eps)

print("Метод простой итерации:")
print(tabulate(
    table,
    headers=["k", "x_k", "x_(k+1)", "|x_(k+1)-x_k|", "f(x_(k+1))"],
    tablefmt="grid",
    floatfmt=".9f"
))

print(f"\nКорень с точностью 10^-6: x = {root:.9f}")