import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy as sp
import random as rand
from statsmodels.stats.weightstats import ztest as ztest
from scipy.stats import ttest_1samp as ttest
from scipy.stats import ttest_ind as ttest2
from scipy.stats import chi2_contingency as chisqk2
#from scipy.stats import chi


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
print("Выборка: ", mas1.tolist())


mas2 = np.random.normal(5, 1, 250)
print("2-ая выборка: ")
print("Среднее: ", np.mean(mas2), "\n",
      "Оценка диссперсии: ", np.var(mas2), "\n",
      "Оценка с.к.о : ", np.std(mas2), '\n',
      "Объём выборки: ", len(mas2), '\n')
print("Выборка: ", mas2.tolist(), "\n\n")


mas = mas1.tolist() + mas2.tolist()
print("Общая выборка:", mas)
print("Среднее: ", np.mean(mas), "\n",
      "Оценка диссперсии: ", np.var(mas), "\n",
      "Оценка с.к.о : ", np.std(mas), '\n',
      "Объём выборки: ", len(mas), '\n')
print("Выборка: ", mas)


print("Для случайной величины Х:")
print("z-sctistic:", ztest(mas1.tolist(), value = 5)[0])
print("p-value: ", ztest(mas1.tolist(), value = 5)[1])
print("t-sctistic:", ttest(mas1.tolist(), 5)[0])
print("p-value: ", ttest(mas1.tolist(), 5)[1])
print("chisqure-statistic(if we know expected value): ", chisqk(mas1)[0])
print("p-value(if we know expected value): ", chisqk(mas1.tolist())[1])
#print("chisqure-statistic(if we don't know expected value): ", chisqk(mas1)[0])
#print("p-value(if we don't know expected value): ", chisqk(mas1.tolist())[1])
print('\n')

print("Для двух случайных величин Х1 и Х2")
print("t-sctistic:", ttest2(mas1.tolist(), mas2.tolist(), equal_var = True)[0])
print("p-value: ", 1 - ttest2(mas1.tolist(), mas2.tolist(), equal_var = True)[1])
print("chisqure-statistic(if we know expected value): ", chisqk2(mas1.tolist(), mas2.tolist())[0])
print("p-value(if we know expected value): ", chisqk2(mas1.tolist(), mas2.tolist())[1])
#print("chisqure-statistic(if we know expected value): ", chisqk(mas1.tolist(), mas2.tolist())[0])
#print("p-value(if we know expected value): ", chisqk(mas1.tolist(), mas2.tolist())[1])
