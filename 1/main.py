import random
import time

start = time.time()


def X(start=1, end=20):
    return [[random.randrange(start, end) for j in range(8)] for i in range(3)]


def Y(x_list, A0=0, A1=1, A2=2, A3=3):
    return [A0 + A1 * x_list[0][i] + A2 * x_list[1][i] + A3 * x_list[2][i] for i in range(8)]


def X0(x_list):
    return [(max(i) + min(i)) / 2 for i in x_list]


def dx(x_list):
    return [max(x_list[i]) - X0(x_list)[i] for i in range(3)]


def Xn(x_list, x0_list, dx_list):
    xn_list = [[(x_list[i][j] - x0_list[i]) / dx_list[i] for j in range(8)] for i in range(3)]
    return xn_list


###base parametrs
a0 = random.randint(0, 10)
a1 = random.randint(0, 10)
a2 = random.randint(0, 10)
a3 = random.randint(0, 10)
###
a = X()
b = Xn(a, X0(a), dx(a))

print("a0 a1 a2 a3")
print(a0, '', a1, '', a2, '', a3)
print('   {:5}{:5}{:5}{:9}{:10}{:8}{:8}'.format('X1', 'X2', 'X3', 'Y', 'Xn1', 'Xn2', 'Xn3'))

for i in range(8):
    print("{:5}{:5}{:5}{:5}{:10.3}{:10.3}{:10.3}".format(a[0][i], a[1][i], a[2][i], Y(a)[i], b[0][i], b[1][i], b[2][i]))

print('\nX0: {0:7} {1:7} {2:7}'.format(*X0(a)))
print('dx: {0:3} {1:3} {2:3}'.format(*dx(a)))
y_et = a0 + a1 * X0(a)[0] + a2 * X0(a)[1] + a3 * X0(a)[2]
print('Yет = {0}'.format(y_et))
print('Варіант 203')
print('max(Y)={0}'.format(max(Y(a))))
print('Виконав: студент групи ІО-92 Гречаний Євгеній')

stop = time.time()
if stop - start == 0:
    print("Час виконання програми менше 0.0000001 секунди")
else:
    print("Час виконання програми: ", str(float(stop) - float(start)), 'секунд')
