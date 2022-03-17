import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import integrate

"""пункт 1"""
print("______________________________________________________________________________________\n")
print("Создать матрицу 5x5 случайных вещественных чисел, принадлежащих интервалу (0, 2).\n "
      "Транспонировать. Вычислить ее определитель.\n")
A = np.random.rand(5, 5) * 2
A_t = A.transpose()
print(A_t)
print("\n")
res = np.linalg.det(A)
print(res)
print("______________________________________________________________________________________\n")
"""пункт 2"""
print("Создать вектор-столбец и матрицу подходящих размеров. Выполнить умножение матриц.")
v_vert_np = np.array([[1], [2]], int)
print(v_vert_np)
print("\n")
C = np.array([[1, 2, 3, 4]], int)
print(C)
print("\n")
res = np.dot(v_vert_np, C)
print(res)
print("______________________________________________________________________________________\n")

"""пункт 3"""
print("Найти собственные векторы и собственные значения")
A = np.array([[0,-3,-1],[3,8,2],[-7,-15,-3]])
print(A)
vals, vecs = np.linalg.eig(A)
print("Значения=\n", vals)
print("Вектор=\n", vecs)
print("______________________________________________________________________________________\n")

"""пункт 4"""
print("Вычислить интеграл")

result = integrate.quad(lambda x: 1/(1 + math.sqrt(2*x + 1)), 0, 4)

print(result)
print("______________________________________________________________________________________\n")

"""пункт 5"""

print("Вычислить интеграл")

def f(x,y):
      return math.cos(x+y)
def h(x):
    return x

result = integrate.dblquad(f, 0, math.pi/2, lambda x: 0, h)

print(result)

print("______________________________________________________________________________________\n")
"""пункт 6"""
print("Построить в одной системе координат графики функций. \n"
      "Оси координат должны быть подписаны, графики должны быть \n"
      "разного цвета, должна быть выведена легенда.")
# Создание объектов артборда и холста

plt.figure(figsize=(8, 5), dpi=80)
ax = plt.subplot(111)

# Мы решили удалить правую и верхнюю прямоугольные границы
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# Установить направление данных на координатной оси
 # 0 согласуется с нашей общей декартовой системой координат, 1 - противоположность
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


# Подготовить данные, использовать распаковку последовательности

X = np.linspace(-2, 2)

C = np.log(X + 5)
L = 3*X-2

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="Ln Function")
plt.plot(X, L, color="red", linewidth=2.5, linestyle="-", label="Lin Function")



plt.xlim(X.min() * 1.1, X.max() * 1.1)

# Изменить метку на оси координат
plt.xticks([-2*np.pi, -3*np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3*np.pi / 2, 2*np.pi ],
           [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3 \pi/2$', r'$+ 2\pi$' ])

plt.ylim(C.min() * 1.1, C.max() * 1.1)
plt.yticks([-2, -1, +1, +2],
           [r'$-2$', r'$-1$', r'$+1$', r'$+2$'])




plt.legend(loc='upper left', frameon=False)
plt.grid()
plt.show()