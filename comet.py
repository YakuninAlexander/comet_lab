import numpy as np
import matplotlib.pyplot as plt

# Инициализация констант
G = 6.674184 * (10 ** -11)
M = 1.9891 * (10 ** 30)
x0 = 1.5 * (10 ** 13) #100 а.е. в м
h = 3.1 * (10 ** 7) #1 год в секундах

def find_T():
    #Из 3 закона Кеплера
    return np.sqrt((x0 ** 3) * (h ** 2) / ((x0/100.0) ** 3))

time = np.arange(0, find_T(), h) # моменты времени полета кометы

def func(t, r):
    x, derX, y, derY = r # derX - производная X, derY - производная Y
    R = np.hypot(x, y) # корень суммы квадратов x,y
    der2X = -(G * M) * (x / R**3) # Вторые производные
    der2Y = -(G * M) * (y / R**3)

    return np.array([derX, der2X, derY, der2Y], float)

def r_init(a, v0): # Инициализация начальных условий
    fx0 = v0 * np.cos(np.radians(a))
    fy0 = v0 * np.sin(np.radians(a))

    return np.array([x0, fx0, 0, fy0], float) # начальные условия

def runge_kutt(t, r): # Метод Рунге-Кутта 4 порядка
    k1 = func(t, r) # Коэффициенты метода
    prom = r + k1 * (h / 2.0)
    k2 = func(t + h / 2.0, prom)
    prom = r + k2 * (h / 2.0)
    k3 = func(t + h / 2.0, prom)
    prom = r + k3 * h
    k4 = func(t + h, prom)

    r += (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4) # Результат для времени t

    return r

def getCometPosition(angle, v0):
    xpositions = []
    ypositions = []

    r = r_init(angle, v0)

    for t in time:
        r = runge_kutt(t, r)
        xpositions.append(r[0]) # Координата кометы х
        ypositions.append(r[2]) # Координата кометы у

    return xpositions, ypositions

def UI():
    while True:
        print('1. Закрутить орбиту.')
        print('2. Определить орбиту кометы для заданной скорости.')
        ans = (int)(input('3. Выход.\n'))
        if (ans == 1):
            x_pos, y_pos = getCometPosition(30, 2000.0)
        elif (ans == 2):
            v0 = (float)(input('Введите начальную скорость кометы: '))
            x_pos, y_pos = getCometPosition(30, v0)
        else:
            return

        fig = plt.figure()
        graf = fig.add_subplot(111)
        graf.plot(x_pos, y_pos)

        c = plt.Circle((0,0), 0.5 * (10 ** 12), color = 'red')
        plt.gca().add_artist(c)
        plt.show()

print("Период кометы: ", find_T())
UI()