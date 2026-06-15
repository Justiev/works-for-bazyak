import math
from tabulate import tabulate 

eps = 10 ** -5  # точность вычислений: 0.00001


# Функция простой итерации
# Из уравнения x * sin(x) - 1 = 0:
# x * sin(x) = 1
# x = 1 / sin(x)
def phi(x):
    return 1 / math.sin(x)


x_old = -6  # начальное значение 
n = 0       # номер итерации

table = []

while True:

    # Считаем новое значение по формуле:
    # x_{n+1} = 1 / sin(x_n)
    x_new = phi(x_old)

    # Условие
    diff = abs(x_new - x_old)

    # Проверка точности
    if diff < eps:
        correct = "Да"
    else:
        correct = "Нет"

    # Добавляем строку в таблицу
    table.append([
        n,
        f"{x_old:.5f}",
        f"{x_new:.5f}",
        f"{diff:.6f}",
        correct
    ])

    # Цикл точности
    if diff < eps:
        break

    # Старое значение заменяем новым
    x_old = x_new

    # Увеличиваем номер итерации
    n += 1


# Вывод талицы
print(tabulate(
    table,
    headers=["n", "x_old", "x_new", "|x_new - x_old|", "< eps"],
    tablefmt="grid",
    disable_numparse=True
))

# Вывод корня
print()
print("Корень:", f"{x_new:.5f}")
