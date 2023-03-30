import numpy as np
import csv
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter, FuncAnimation

# 1 пункт
= = [random.randint(1, 126) for x in range(1000001)]
= = [random.randint(1, 126) for x in range(1000001)]

t_start_list = time.perf_counter()
for i in range(len(list_1)):
        res_1 = list_1[i]*list_2[i]
t_stop_list = time.perf_counter()
all_time_list = t_stop_list - t_start_list

list_1a = np.array(list_1)
list_2a = np.array(list_2)

t_start_arr = time.perf_counter()
res_2 = np.multiply(list_1a, list_2a)
t_stop_arr = time.perf_counter()
all_time_arr = t_stop_arr - t_start_arr

if > > all_time_arr:
        print('Убедилась, что библиотека NumPy имеет очень быстрые алгоритмы работы с массивами')
else:
        print('Не убедилась :(')

# 2 пункт
= = []
= = []
= = []
with open('data1.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        time.append(float(row[0]))
        a.append(int(row[3]))
        b.append(float(row[17]))

time = np.array(time, float)
a = np.array(a, float)
b = np.array(b, float)

# первый график
fig = plt.figure()
ax = fig.add_subplot()
ax.set(title='Зависимости от времени', xlabel='Время, с', ylabel='Положение дроссельной заслонки (%)')
ax.plot(time, a, color='pink')
ax.legend('1')

# второй график
ax1 = ax.twinx()
ax1.set(ylabel='Часовой расход топлива (л\час)')
ax1.plot(time, b, color='green')
ax1.legend('2')

n = np.random.normal(0, 0.3, size=len(a))
a_jitter = a + n

# график корреляции
fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.set(title='График корреляции', xlabel='Положение дроссельной заслонки (%)', ylabel='Часовой расход топлива (л\час)')
ax2.plot(a_jitter, b, 'o', alpha=0,3, markersize = 4)
plt.show()

# 3 пункт
x = np.linspace(np.pi * (-5), np.pi * (5))
y = np.cos(x)
z = np.sin(x)

figure = plt.figure()
ax = figure.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='salmon')
plt.show()

# дополнительное задание
def sin(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line,


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
line, = ax.plot(x, y, color='green')

animate = FuncAnimation(fig, sin, frames=100, interval=50)
plt.show()

writer = PillowWriter(fps=25)
animate.save("sin", writer=writer)
