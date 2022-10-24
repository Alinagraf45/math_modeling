from scipy import integrate
from math import *
import numpy as np
import random
import matplotlib.pyplot as plt

global all
all = 0
def punkt1():
    global all
    def integrals1(t):
        return 9*(sin(2*pi*t)) + 9

    def integrals2(t):
        return 9/t

    def integrals3(t):
        return -18*t**2 + 72*t - 67.5

    a = integrate.quad(integrals1, 0, 1)[0]
    v = integrate.quad(integrals2, 1, 2)[0]
    k = integrate.quad(integrals3, 2, 3)[0]
    all = (v + a + k)

    x1 = np.arange(0, 1, 0.001)
    x2 = np.arange(1, 2, 0.001)
    x3 = np.arange(2, 3, 0.001)

    alina = []
    for i in x1:
        alina.append(integrals1(i))

    plt.plot(x1, alina, label='9*(sin(2*pi*t)) + 9')
    plt.plot(x2, integrals2(x2), label='9/t')
    plt.plot(x3, integrals3(x3), label='-18*t**2 + 72*t - 67.5')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.show()

    print('Значение интеграла встроенной функцией: ', all)
    return all

def monte_karlo():
    mas_x = []
    mas_y = []

    for j in range(0, 15):
        n = 2 ** j

        count = 0

        for i in range(0, n):
            x = random.uniform(0.0, 3.0)

            if x < 1:
                count += 9 * (sin(2 * pi * x)) + 9

            if 1 <= x <= 2:
                count += 9/x

            if x > 2:
                count += -18 * x ** 2 + 72 * x - 67.5

        integral_value = (3.0/n) * count

        print('Интеграл методом Монте-Карло:', integral_value)

        mas_x.append(n)
        mas_y.append(integral_value)
        print('При N =', n, 'значение F =', integral_value)

    fig, ax = plt.subplots()
    ax.hlines(all, -5, 10000, color = 'r')
    plt.plot(mas_x, mas_y)
    plt.legend(['истинное значение F'])

    plt.semilogx(basey=2)

    ax.set_xlabel('N повторений')
    ax.set_ylabel('значение F')
    plt.show()

if __name__ == '__main__':
    punkt1()
    monte_karlo()