from tabulate import tabulate


# Функция
def f(x):
    return x**3 - 3 * x**2 - 24 * x + 1


# Первая производная
def df(x):
    return 3 * x**2 - 6 * x - 24


# Вторая производная
def df2(x):
    return 6 * x - 6


# Округление до 10^-6
def fmt(x):
    return f"{x:.6f}"


def solve_combined(a, b, eps):
    # Определяем, где будет касательная, а где хорда
    if f(a) * df2(a) > 0:
        x_k, x_n = a, b
    else:
        x_k, x_n = b, a

    table = []
    iteration = 0

    while abs(x_n - x_k) > eps:
        old_x_n = x_n
        old_x_k = x_k

        # Метод хорд
        x_n_new = x_n - (f(x_n) * (x_k - x_n)) / (f(x_k) - f(x_n))

        # Метод касательных
        x_k_new = x_k - f(x_k) / df(x_k)

        # Разница между новыми значениями
        diff = abs(x_n_new - x_k_new)

        if diff < eps:
            correct = "Да"
        else:
            correct = "Нет"

        # Добавляем строку в таблицу
        # Теперь первая итерация будет 0
        table.append([
            iteration,
            fmt(old_x_n),
            fmt(old_x_k),
            fmt(x_n_new),
            fmt(x_k_new),
            fmt(diff),
            correct
        ])

        # Обновляем значения
        x_n = x_n_new
        x_k = x_k_new

        # Увеличиваем номер итерации только после записи строки
        iteration += 1

    print(tabulate(
        table,
        headers=[
            "Итерация",
            "x_n",
            "x_k",
            "x_n новое",
            "x_k новое",
            "|x_n - x_k|",
            "< eps"
        ],
        tablefmt="grid",
        disable_numparse=True
    ))

    root = (x_n + x_k) / 2

    print()
    print("Найденный корень уравнения:", fmt(root))


# Изначальные параметры
a = 0
b = 1
eps = 10 ** -6

solve_combined(a, b, eps)