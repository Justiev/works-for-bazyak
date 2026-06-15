import numpy as np
import matplotlib.pyplot as plt

# функции (рисунок 2.9)
def f_a(x): return 6 - x**2
def df_a(x): return -2 * x
ddf_a = -2


def f_b(x): return 2 / x - 0.5
def df_b(x): return -2 / (x**2)
ddf_b = 2


def f_v(x): return x**2 - 2
def df_v(x): return 2 * x
ddf_v = 2


def f_g(x): return np.log(x/0.4) - 1.5
def df_g(x): return 1 / x
ddf_g = -0.5


fig, axs = plt.subplots(2, 2, figsize=(10, 10))     # subplots - позволяет размещать несколько независимых графиков в одном окне.
plt.subplots_adjust(hspace=0.4)     # Увеличивает вертикальное расстояние между строками в сетке.

# ось x
a, b = 0.5, 2.5
x_axis = np.linspace(0.1, 3.0, 100)


configs = [
    (f_a, df_a, ddf_a, 'а', "f' < 0, f'' < 0"),
    (f_b, df_b, ddf_b, 'б', "f' < 0, f'' > 0"),
    (f_v, df_v, ddf_v, 'в', "f' > 0, f'' > 0"),
    (f_g, df_g, ddf_g, 'г', "f' > 0, f'' < 0")
]


for i, (f, df, ddf, name, desc) in enumerate(configs):
    ax = axs.flat[i]
    
    ax.plot(x_axis, f(x_axis), color='blue', label='График f(x)')
    ax.axhline(0, color='black', linewidth=1)
    

    # КАСАТЕЛЬНАЯ (Рисунок 2.10)
    # Выбираем x0 так, чтобы f(x0) и f''(x0) были одного знака
    if f(a) * ddf > 0:
        x0 = a
    else:
        x0 = b
    
    x_tangents = x0 - f(x0) / df(x0)
    ax.plot([x0, x_tangents], [f(x0), 0], color='red', label='Касательная', linewidth=2)
    

    # ХОРДА (Рисунок 2.11)
    # Соединяет точки (a, f(a)) и (b, f(b))
    x_chord = a - f(a) * (b - a) / (f(b) - f(a))
    ax.plot([a, b], [f(a), f(b)], color='green', linestyle='--', label='Хорда')
    

    # Оформление
    ax.set_title(f"График {name}: {desc}")
    ax.set_xticks([a, b])
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.show()
