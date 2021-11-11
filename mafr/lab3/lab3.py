from math import sqrt

prices = {'10-09-2021': [332.75, 327.41, 420.5, 1728.63],
          '13-09-2021': [338.98, 326.48, 570, 1765.29],
          '14-09-2021': [343.34, 333.51, 724.5, 1731.85],
          '15-09-2021': [338.5, 326.99, 664, 1768.68],
          '16-09-2021': [334.5, 329.56, 600.5, 1756.18],
          '17-09-2021': [325.7, 326.92, 551, 1717],
          '20-09-2021': [335.3, 323.25, 605, 1710.6],
          '21-09-2021': [340.59, 327.8, 702, 1730],
          '22-09-2021': [343.47, 327.02, 801, 1752],
          '23-09-2021': [344.29, 325.44, 825, 1751],
          '24-09-2021': [355.19, 331.68, 986, 1765.25]}

prices_lst = list(prices.values())
# prices_extra_lst = list(prices_extra.values())

N = len(prices_lst) - 1

x_1 = (1/15, 2/15, 1 - 3/15)
x_2 = (1 - 3/15, 2/15, 1/15)

factor_lst_x = [(prices_lst[i + 1][0] - prices_lst[i][0]) / prices_lst[i][0] for i in range(N)]
factor_lst_y = [(prices_lst[i + 1][1] - prices_lst[i][1]) / prices_lst[i][1] for i in range(N)]
factor_lst_z = [(prices_lst[i + 1][2] - prices_lst[i][2]) / prices_lst[i][2] for i in range(N)]

Tx = sum(factor_lst_x) / N
Ty = sum(factor_lst_y) / N
Tz = sum(factor_lst_z) / N

c11 = sum(el**2 - 2*el*Tx + Tx**2 for el in factor_lst_x) / (N - 1)  # S2x
c22 = sum(el**2 - 2*el*Ty + Ty**2 for el in factor_lst_y) / (N - 1)  # S2y
c33 = sum(el**2 - 2*el*Tz + Tz**2 for el in factor_lst_z) / (N - 1)  # S2z

c12 = (sum((factor_lst_x[i] - Tx) * (factor_lst_y[i] - Ty) for i in range(N)) / (N - 1))
c13 = (sum((factor_lst_x[i] - Tx) * (factor_lst_z[i] - Tz) for i in range(N)) / (N - 1))
c23 = (sum((factor_lst_y[i] - Ty) * (factor_lst_z[i] - Tz) for i in range(N)) / (N - 1))

C = [[c11, c12, c13], [c12, c22, c23], [c13, c23, c33]]
print("C")
for el in C:
    print(el)

E1 = x_1[0] * Tx + x_1[1] * Ty + x_1[2] * Tz
E2 = x_2[0] * Tx + x_2[1] * Ty + x_2[2] * Tz
print(f"\nE1 = {E1}  E2 = {E2}")

V1 = c11 * x_1[0]**2 + c22 * x_1[1]**2 + c33 * x_1[2]**2 + 2 * c12 * x_1[0] * x_1[1] + 2 * c23 * x_1[1] * x_1[2]
V2 = c11 * x_2[0]**2 + c22 * x_2[1]**2 + c33 * x_2[2]**2 + 2 * c12 * x_2[0] * x_2[1] + 2 * c23 * x_2[1] * x_2[2]
print(f"V1 = {V1}  V2 = {V2}")

V1sqrt = sqrt(V1)
V2sqrt = sqrt(V2)
print(f"σ1 = {V1sqrt}  σ2 = {V2sqrt}")
