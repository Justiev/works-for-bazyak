import math
from tabulate import tabulate


# Основная функция
# Нужно найти x, при котором f(x) = 0
def f(x):
    return 2 ** (-x) - math.sin(x)


# Первая производная функции f(x)
def df(x):
    return -math.log(2) * 2 ** (-x) - math.cos(x)


# Вторая производная функции f(x)
def ddf(x):
    return (math.log(2) ** 2) * 2 ** (-x) + math.sin(x)


# Комбинированный метод хорд и касательных
def chord_tangent_method(a, b, eps):

    table = []

    # Номер итерации
    k = 0

    # Проверяем, есть ли корень на отрезке
    if f(a) * f(b) > 0:
        print("На этом отрезке нет смены знака.")
        return None

    # Выбираем точку для метода касательных
    if f(a) * ddf(a) > 0:
        x_tangent = a   # точка для касательной
        x_chord = b     # точка для хорды
    else:
        x_tangent = b   # точка для касательной
        x_chord = a     # точка для хорды

    # Работаем, пока расстояние между двумя приближениями больше точности
    while abs(x_tangent - x_chord) > eps:
        # Сохраняем старые значения
        old_tangent = x_tangent
        old_chord = x_chord

        # Формула метода касательных:
        # x_new = x - f(x) / f'(x)
        x_tangent = old_tangent - f(old_tangent) / df(old_tangent)

        # Формула метода хорд
        x_chord = old_chord - f(old_chord) * (old_tangent - old_chord) / (
            f(old_tangent) - f(old_chord)
        )

        # Добавляем данные шага в таблицу
        table.append([
            k,                              
            old_tangent,                    
            old_chord,                      
            x_tangent,                      
            x_chord,                        
            abs(x_tangent - x_chord)        
        ])

        # Увеличиваем номер итерации
        k += 1

    root = (x_tangent + x_chord) / 2

    # Возвращаем корень и таблицу
    return root, table


a = 0.67
b = 0.68
eps = 10 ** (-6)

# Запускаем комбинированный метод
result = chord_tangent_method(a, b, eps)

# Если метод сработал
if result is not None:

    root, table = result

    print("Комбинированный метод хорд и касательных:")
    print(tabulate(
        table,
        headers=[
            "k",
            "старое x кас.",
            "старое x хорды",
            "новое x кас.",
            "новое x хорды",
            "|разность|"
        ],
        tablefmt="grid",
        floatfmt=".9f"
    ))

    print(f"\nКорень с точностью 10^-6: x = {root:.9f}")