import numpy as np

v = [np.array([4.,1.,3.,-1.]),
    np.array([2.,1.,-3.,4.]),
    np.array([1.,0.,-2.,7.]),
    np.array([6., 2., 9., -5.])]

mu = []
# for i in range(4):
#     mu.append([])
#     for j in range(i):
#         mu[i].append(v[i].dot(v[j]) / v[j].dot(v[j]))

u = []
for i in range(4):
    mu.append([])
    sum = v[i]
    for j in range(i):
        mu[i].append(v[i].dot(u[j]) / u[j].dot(u[j]))
        sum -= mu[i][j] * u[j]
    u.append(sum)

print(u)

