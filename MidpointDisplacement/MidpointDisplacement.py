import matplotlib.pyplot as plt
import random


def f(x):
    return x * x


def midpoint_displacement(xL, yL, xR, yR, roughness, threshold):
    if abs(xR - xL) < threshold:
        return [(xL, yL), (xR, yR)]

    xM = (xL + xR) / 2
    yM = (yL + yR) / 2 + (random.random() * 2 - 1) * roughness * abs(xR - xL)

    left_segment = midpoint_displacement(xL, yL, xM, yM, roughness, threshold)
    right_segment = midpoint_displacement(xM, yM, xR, yR, roughness, threshold)

    return left_segment + right_segment[1:]


def generate_terrain(width, height, roughness, threshold):
    terrain = midpoint_displacement(0, height // 2, width, height // 2, roughness, threshold)
    return terrain


def plot(terrain, C, f=None):
    x = [point[0] for point in terrain]
    if f is not None:
        y = [f(point[1]) + C for point in terrain]
    else:
        y = [point[1] + C for point in terrain]

    plt.fill_between(x, y, min(y) - 10, color='black')
    plt.fill_between(x, y, max(y) + 10, color='blue')
    plt.plot(x, y, color='green')

    plt.axis('off')
    plt.show()


# Настройки
width = 500  # Ширина изображения
height = 500  # Высота изображения
threshold = int(input('Введите пороговое значение длины отрезка (целое число) '))
roughness = float(input('Введите параметр шероховатости '))
C = float(input('Введите константу для построцессинга (0 - без построцессинга) '))
is_f = input('Желаете ли вы использовать функцию f(x) = x^2 в качестве построцессинга высот? 1 - Да, 0 - нет. ')

points = generate_terrain(width, height, roughness, threshold)

if is_f == '1':
    plot(points, C, f)
else:
    plot(points, C)
