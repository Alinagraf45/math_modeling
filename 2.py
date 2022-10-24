from math import *
import numpy as np
import random
from scipy.stats import norm
import matplotlib.pyplot as plt
import time

def main():
    start_time = time.time()
    mass = np.array([])  # массив выборки – пустой
    mean, sd = 0, 1 # мат ожидание всегда равно 0, дисперсия всегда равна 1
    n = 0 # количество элементов выборки
    delta = 0
    x_min, x_max = 0, 0
    grafic = np.zeros(10)
    M = np.array([])
    D = np.array([])
    N = np.array([])

    while min(grafic) < 100:
        n += 1
        x = random.uniform(0.0, 1.0)
        x1 = random.uniform(0.0, 1.0)
        # две независимые случайных величины, распределенных по нормальному закону
        alph = sqrt(-2*np.log(x)) * sin(2*pi*x1)
        alph1 = sqrt(-2*np.log(x)) * cos(2*pi*x1)
        mass = np.insert(mass, len(mass), alph)
        mass = np.insert(mass, len(mass), alph1)

        P = (2*n - np.sum(grafic)) / 2*n

        if P >= 0.01: # Пересчет всех Ni
            grafic = [0] * 10
            x_min = np.amin(mass)
            x_max = np.amax(mass)
            delta = (x_max - x_min) / 10
            for i in mass: # подсчет кол-ва вхождений элементов в интервалы
                k = floor((i - x_min)/delta)
                if k == 10:
                    k = 9
                if 9 >= k >= 0:
                    grafic[k] += 1
            print(grafic)
        else:
            for i in range(1, 3): # нахождение номера интервала сгенерированных чисел
                k = floor((mass[-i] - x_min) / delta)
                if k == 10:
                    k = 9
                if 9 >= k >= 0:
                    grafic[k] += 1
            print(grafic)

        if n % 100 == 0:
            M = np.insert(M, len(M), np.mean(mass)) # мат ожидание на каждом сотом шаге цикла
            D = np.insert(D, len(D), np.var(mass)) # дисперсия на каждом сотом шаге цикла
            N = np.insert(N, len(N), n) # количество элементов

    print('Количество чисел:', n)
    print('Количество вхождений в интервалы', grafic)
    print('Минимальное число:', x_min, 'Максимальное число:', x_max)
    print('Вреся работы программы:', time.time() - start_time)


    x = []
    y = []
    x.append(x_min + delta/2)

    for i in range(9):
        x.append(x[i] + delta)

    for i in range(0, 10):
        y.append(grafic[i] / ((2*n)*delta))
    print(x)
    print(y)

    # график гистограммы и плотности распределения
    plt.xlabel('Интервалы')
    plt.ylabel('Количество вхождений в интервалы')
    line = np.linspace(x_min, x_max, 100)
    plt.plot(line, norm.pdf(line, loc=0, scale=sqrt(sd)), color='red')
    plt.bar(x, y, width=delta)
    plt.title('Гистограмма сформированной выборки')
    plt.show()

    # график мат ожидания
    x = np.arange(0, len(N), 1)
    plt.figure(3)
    plt.plot(x, M)
    plt.plot(range(0, len(x)), [mean for i in range(0, len(x))])
    plt.title("Мат ожидание")
    plt.xlabel('размер выборки')
    plt.ylabel('мат. ожидание')
    plt.show()

    # график дисперсии
    plt.figure(4)
    plt.plot(x, D)
    plt.plot(range(0, len(x)), [sd for i in range(0, len(x))])
    plt.title("Дисперсия")
    plt.xlabel('размер выборки')
    plt.ylabel('дисперсия')
    plt.show()

main()
