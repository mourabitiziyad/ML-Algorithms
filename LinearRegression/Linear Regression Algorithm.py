from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

def create_dataset(hm, variance, correlation ,step=2):
    val = 1
    Ys = []
    for _ in range(hm):
        y = val + random.randrange(-variance, variance)
        Ys.append(y)
        if correlation == 'pos':
            print('yes')
            val += step
        elif correlation == 'neg':
            print('yes')
            val -= step
    Xs = [i for i in range(len(Ys))]
    print("Ys are: ", Ys)
    print("Xs are: ", Xs)
    return np.array(Xs, dtype=np.float64), np.array(Ys, dtype=np.float64)

def best_fit_line(Xs, Ys):
    m = (mean(Xs) * mean(Ys) - mean(Xs * Ys)) / ((mean(Xs)**2) - mean(Xs**2))
    b = mean(Ys) - m * mean(Xs)
    return m, b

def squared_error(Ys_orig, Ys_line):
    return sum((Ys_line - Ys_orig)**2)

def coef_determination(Ys_orig, Ys_line):
    y_mean_line = [mean(Ys_orig) for y in Ys_orig]
    squared_error_regr = squared_error(Ys_orig, Ys_line)
    squared_error_y_mean = squared_error(Ys_orig, y_mean_line)

    return 1 - (squared_error_regr / squared_error_y_mean)

Xs, Ys = create_dataset(40, 40, 'neg',2)


m, b = best_fit_line(Xs, Ys)
print(m, b)

regression_line = [(m*x) + b for x in Xs]

r_squared = coef_determination(Ys, regression_line)
print(r_squared)

plt.scatter(Xs, Ys)
plt.plot(Xs, regression_line)
plt.show()

