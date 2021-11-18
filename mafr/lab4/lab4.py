from math import sqrt
from sympy import symbols
from scipy import stats

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

ADEKVAT = "Fn >= Fkr --> модель адекватная"
NEADEKVAT = "Fn < Fkr --> модель неадекватная"


prices_lst = list(prices.values())
# prices_extra_lst = list(prices_extra.values())

N = len(prices_lst) - 1

factor_lst_x = [(prices_lst[i + 1][0] - prices_lst[i][0]) / prices_lst[i][0] for i in range(N)]
factor_lst_y = [(prices_lst[i + 1][1] - prices_lst[i][1]) / prices_lst[i][1] for i in range(N)]
factor_lst_z = [(prices_lst[i + 1][2] - prices_lst[i][2]) / prices_lst[i][2] for i in range(N)]
factor_lst_i = [(prices_lst[i + 1][3] - prices_lst[i][3]) / prices_lst[i][3] for i in range(N)]

print("Однофакторная модель")
for i in range(N):
    print(f"r{i + 1} ", factor_lst_x[i], factor_lst_y[i], factor_lst_z[i], factor_lst_i[i])


Tx = sum(factor_lst_x) / N
Ty = sum(factor_lst_y) / N
Tz = sum(factor_lst_z) / N
Ti = sum(factor_lst_i) / N
print(f"\nT --> {Tx, Ty, Tz, Ti}")

S2x = sum(el**2 - 2*el*Tx + Tx**2 for el in factor_lst_x) / (N - 1)
S2y = sum(el**2 - 2*el*Ty + Ty**2 for el in factor_lst_y) / (N - 1)
S2z = sum(el**2 - 2*el*Tz + Tz**2 for el in factor_lst_z) / (N - 1)
S2i = sum(el**2 - 2*el*Ti + Ti**2 for el in factor_lst_i) / (N - 1)
print(f"S2 --> {S2x, S2y, S2z, S2i}")

Sx = sqrt(S2x)
Sy = sqrt(S2y)
Sz = sqrt(S2z)
Si = sqrt(S2i)
print(f"S --> {Sx, Sy, Sz, Si}")


rxi = (sum((factor_lst_x[i] - Tx) * (factor_lst_i[i] - Ti) for i in range(N)) / (N - 1)) / (Sx * Si)
ryi = (sum((factor_lst_y[i] - Ty) * (factor_lst_i[i] - Ti) for i in range(N)) / (N - 1)) / (Sy * Si)
rzi = (sum((factor_lst_z[i] - Tz) * (factor_lst_i[i] - Ti) for i in range(N)) / (N - 1)) / (Sz * Si)
print(f"\nr1,Ri = {rxi}, r2,Ri = {ryi}, r3,Ri = {rzi}")


print("\nri-μi=ρiI*(Si/SI)*(RI-μI)")
Ri = symbols('Ri')
print(f"rx = {Tx + rxi * (Sx / Si) * (Ri - Ti)}\n"
      f"ry = {Ty + ryi * (Sy / Si) * (Ri - Ti)}\n"
      f"rz = {Tz + rzi * (Sz / Si) * (Ri - Ti)}\n")

B = [rxi * (Sx / Si), ryi * (Sy / Si), rzi * (Sz / Si)]
print(B)
print(f"μ1 = {Tx}\n"
      f"μ2 = {Ty}\n"
      f"μ3 = {Tz}\n")

C = []
for i in B:
    row = []
    for j in B:
        row.append(i * j * S2i)
    C.append(row)

print("C")
for el in C:
    print(el)

x_1 = (1/15, 2/15, 1 - 3/15)
x_2 = (1 - 3/15, 2/15, 1/15)
print(x_1)
print(x_2)

E1 = x_1[0] * Tx + x_1[1] * Ty + x_1[2] * Tz
E2 = x_2[0] * Tx + x_2[1] * Ty + x_2[2] * Tz
print(f"\nE1 = {E1}  E2 = {E2}")

V1 = C[0][0] * x_1[0]**2 + \
     C[1][1] * x_1[1]**2 + \
     C[2][2] * x_1[2]**2 + \
     2 * C[0][1] * x_1[0] * x_1[1] + \
     2 * C[0][2] * x_1[0] * x_1[2] + \
     2 * C[1][2] * x_1[1] * x_1[2]

V2 = C[0][0] * x_2[0]**2 + \
     C[1][1] * x_2[1]**2 + \
     C[2][2] * x_2[2]**2 + \
     2 * C[0][1] * x_2[0] * x_2[1] + \
     2 * C[0][2] * x_2[0] * x_2[2] + \
     2 * C[1][2] * x_2[1] * x_2[2]
print(f"V1 = {V1}  V2 = {V2}")

V1sqrt = sqrt(V1)
V2sqrt = sqrt(V2)
print(f"σ1 = {V1sqrt}  σ2 = {V2sqrt}")
