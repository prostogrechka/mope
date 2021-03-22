import random
import numpy as np


def F(disp):
    return [func(disp[0], disp[1]),
     func(disp[2], disp[0]),
     func(disp[2], disp[1])]

def O(F):
    return [(((m - 2) / m) * F[0]),
     (((m - 2) / m) * F[1]),
     (((m - 2) / m) * F[2])]

def func(a, b):
    if a > b:
        return a / b
    else:
        return b / a

def R(O):
    return [((abs(O[0] - 1) / 1.7888543819998317)),
     ((abs(O[1] - 1) / 1.7888543819998317)),
     ((abs(O[2] - 1) / 1.7888543819998317))]


### base parametrs
m = 10
romanovskii_koef = [1.69, 2, 2, 2, 2, 2.17, 2.17, 2.29, 2.29, 2.39, 2.39,
                    2.39, 2.49, 2.49,
                    2.49, 2.49, 2.62, 2.62, 2.62]
x1_min, x1_max = -20, 30
x2_min, x2_max = -25, 10
y_max, y_min = 270, 170

y = [[random.randint(y_min, y_max) for j in range(m)] for i in range(3)]
y_ser = [sum(i) / m for i in y]

xn = [[-1, -1], [-1, 1], [1, -1]]
mx = [((xn[0][0] + xn[1][0] + xn[2][0]) / 3),
      ((xn[0][1] + xn[1][1] + xn[2][1]) / 3)]
my = sum(y_ser) / len(y_ser)

vidhilenya = 1.7888543819998317


disp = [*map(np.var, y)]
###

F = F(disp)

O = O(F)

R = R(O)

a_1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
a_2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
a_3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3
a_11 = (xn[0][0] * y_ser[0] + xn[1][0] * y_ser[1] + xn[2][0] * y_ser[2]) / 3
a_22 = (xn[0][1] * y_ser[0] + xn[1][1] * y_ser[1] + xn[2][1] * y_ser[2]) / 3

b_0 = (np.linalg.det([[my, mx[0], mx[1]], [a_11, a_1, a_2], [a_22, a_2, a_3]]) / np.linalg.det(
    [[1, mx[0], mx[1], ], [mx[0], a_1, a_2], [mx[1], a_2, a_3]]))
b_1 = (np.linalg.det([[1, my, mx[1]], [mx[0], a_11, a_2], [mx[1], a_22, a_3]]) / np.linalg.det(
    [[1, mx[0], mx[1]], [mx[0], a_1, a_2], [mx[1], a_2, a_3]]))
b_2 = (np.linalg.det([[1, mx[0], my], [mx[0], a_1, a_11], [mx[1], a_2, a_22]]) / np.linalg.det(
    [[1, mx[0], mx[1]], [mx[0], a_1, a_2], [mx[1], a_2, a_3]]))

dif_x1 = abs(x1_max - x1_min) / 2
dif_x2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2
a0 = b_0 - (b_1 * x10 / dif_x1) - (b_2 * x20 / dif_x2)
a1 = b_1 / dif_x1
a2 = b_2 / dif_x2

yn1 = a0 + a1 * x1_min + a2 * x2_min
yn2 = a0 + a1 * x1_max + a2 * x2_min
yn3 = a0 + a1 * x1_min + a2 * x2_max

print("Y")
for i in y:
    for j in i:
        print(j, end =' ')
    print()
print()
print('Середнє значення функції відгуку в рядках: ', *y_ser)
print('Дисперсії по рядках: ', *disp)
print('Oсновне відхилення: ', vidhilenya)
print()
for i in range(len(F)):
    print('Fu' + str(i) + ': ', F[i])
print()
for i in range(len(O)):
    print('Ou' + str(i) + ': ', O[i])
print()
for i in range(len(R)):
    print('Ru' + str(i) + ': ', R[i])
print("Критерій Романовського = ", romanovskii_koef[m - 2] )

#перевірка на однорідність
for i in R:
    if R[0] > romanovskii_koef[m - 2]:
        print('Дисперсія не є однорідною')
else:
    print('Дисперсія є однорідною')

print()
print(b_0, b_1, b_2)
if [round((b_0 - b_1 - b_2)), round((b_0 + b_1 - b_2)), round((b_0 - b_1 + b_2))] == [*map(round, [yn1, yn2, yn3])]:
    print("Перевірка успішна.")
    print([round((b_0 - b_1 - b_2)), round((b_0 + b_1 - b_2)), round((b_0 - b_1 + b_2))])
    print([*map(round, [yn1, yn2, yn3])])
else:
    print([round((b_0 - b_1 - b_2)), round((b_0 + b_1 - b_2)), round((b_0 - b_1 + b_2))])
    print([*map(round, [yn1, yn2, yn3])])
    print("Перевірка не успішна.")
print('Виконав: студент групи ІО-92 Гречаний Євгеній')