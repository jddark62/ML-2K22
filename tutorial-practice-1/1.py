import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def sklearn_regression(x, y):
    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)

    linreg = LinearRegression().fit(x,y)
    print('Intercept obtained from formula: ')
    print(linreg.intercept_)
    print('Slope obtained from formula: ')
    print(linreg.coef_)

x = np.array([2, 3, 5, 7, 9])
y = np.array([4, 5, 7, 10, 15])
#correlation coefficient
rho = np.corrcoef(x, y)
print(rho)

#least of squares

#calculating mean
mean_x = np.mean(x)
mean_y = np.mean(y)
n = len(x)

#calculate slope and intercept
xy = []

for i, value in enumerate(x):
    xy.append(x[i] * y[i])

x_sqr = [i**2 for i in x]
n = len(x)

slope = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x_sqr) - sum(x)**2)
intercept = (sum(y) - slope*sum(x))/n
print(intercept)
print(slope)

#mean squared error
mse = mean_squared_error(y, intercept + slope*x, squared = False)
print(mse)

#box plot
plt.boxplot(x)
plt.show()