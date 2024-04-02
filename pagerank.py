import numpy as np
from fractions import Fraction as f

dp = f(1, 3)
m = np.matrix([[0, 0, 1], [f(1, 2), 0, 0], [f(1, 2), 1, 0]])
ex = np.zeros((3, 3))
ex[:] = dp

b = 0.7
a = b * m + ((1 - b) * ex)

r = np.matrix([dp, dp, dp]).transpose()
prev_r = r

for i in range(1, 100):
    r = a * r
    res = np.round((r).astype(float), decimals=3)
    print(res)
    if (prev_r == r).all():
        break
    prev_r = r

print("Final:", res)
print("sum", np.sum(r))


#pip install numpy
#python.exe -m pip install --upgrade pip –user
