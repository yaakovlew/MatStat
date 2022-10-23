import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy as sp
import random as rand

x = np.arange(0, 10, 0.001)

plt.plot(x, norm.pdf(x, 5, 3))
plt.plot(x, norm.pdf(x, 5, 1), color='red')
plt.show()

mas1 = np.random.normal(5, 3 ** (0.5), 250)
print("1-ая выборка: ")
print("Среднее: ", np.mean(mas1), "\n",
      "Оценка диссперсии: ", np.var(mas1), "\n",
      "Оценка с.к.о : ", np.std(mas1), '\n',
      "Объём выборки: ", len(mas1), '\n')


mas2 = np.random.normal(5, 1, 250)
print("2-ая выборка: ")
print("Среднее: ", np.mean(mas2), "\n",
      "Оценка диссперсии: ", np.var(mas2), "\n",
      "Оценка с.к.о : ", np.std(mas2), '\n',
      "Объём выборки: ", len(mas2), '\n')


mas = mas1.tolist() + mas2.tolist()
print("Общая выборка:")
print("Среднее: ", np.mean(mas), "\n",
      "Оценка диссперсии: ", np.var(mas), "\n",
      "Оценка с.к.о : ", np.std(mas), '\n',
      "Объём выборки: ", len(mas), '\n')

