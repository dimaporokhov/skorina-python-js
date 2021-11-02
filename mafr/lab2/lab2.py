from math import log, exp, sqrt
from sympy import solve, symbols

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

prices_extra = {'27-09-2021': [354.07, 329.3, 968, 1785],
                '28-09-2021': [360.88, 328.43, 992, 1750],
                '29-09-2021': [360.8, 340.99, 903.5, 1768.1],
                '30-09-2021': [363.25, 338.48, 987.5, 1762.3],
                '01-09-2021': [376.06, 345.85, 134.5, 1775.5]}

# случайные значения
En = [0.523532435, -1.238524874, -0.220835545, 0.789807473, 0.475431534, 0.895547601]

prices_lst = list(prices.values())
prices_extra_lst = list(prices_extra.values())

N = len(prices_lst) - 1

factor_lst = [[(prices_lst[i + 1][0] - prices_lst[i][0]) / prices_lst[i][0],
               (prices_lst[i + 1][1] - prices_lst[i][1]) / prices_lst[i][1],
               (prices_lst[i + 1][2] - prices_lst[i][2]) / prices_lst[i][2],
               (prices_lst[i + 1][3] - prices_lst[i][3]) / prices_lst[i][3]]
              for i in range(N)]

print("Однофакторная модель")
for i, el in enumerate(factor_lst):
    print(f"r{i + 1} ", *el)


hx = [log(prices_lst[i + 1][0] / prices_lst[i][0]) for i in range(N)]
hy = [log(prices_lst[i + 1][1] / prices_lst[i][1]) for i in range(N)]
hz = [log(prices_lst[i + 1][2] / prices_lst[i][2]) for i in range(N)]
hn = [log(prices_lst[i + 1][3] / prices_lst[i][3]) for i in range(N)]

Tx = sum(hx) / N
Ty = sum(hy) / N
Tz = sum(hz) / N
Tn = sum(hn) / N
print(f"\nT --> {Tx, Ty, Tz, Tn}")

S2x = sum(el**2 - 2*el*Tx + Tx**2 for el in hx) / (N - 1)
S2y = sum(el**2 - 2*el*Ty + Ty**2 for el in hy) / (N - 1)
S2z = sum(el**2 - 2*el*Tz + Tz**2 for el in hz) / (N - 1)
S2n = sum(el**2 - 2*el*Tn + Tn**2 for el in hn) / (N - 1)
print(f"S2 --> {S2x, S2y, S2z, S2n}")

Sx = sqrt(S2x)
Sy = sqrt(S2y)
Sz = sqrt(S2z)
Sn = sqrt(S2n)
print(f"S --> {Sx, Sy, Sz, Sn}")


# rxy = ((sum(el[0] * el[1] for el in factor_lst) - Tx * Ty) / N) / (Sx * Sy)
# rxz = ((sum(el[0] * el[2] for el in factor_lst) - Tx * Tz) / N) / (Sx * Sz)
# ryz = ((sum(el[1] * el[2] for el in factor_lst) - Ty * Tz) / N) / (Sy * Sz)
# print(f"\nr1,2 = {rxy}, r1,3 = {rxz}, r2,3 = {ryz}")

rxn = ((sum(el[0] * el[3] for el in factor_lst) - Tx * Tn) / N) / (Sx * Sn)
ryn = ((sum(el[1] * el[3] for el in factor_lst) - Ty * Tn) / N) / (Sy * Sn)
rzn = ((sum(el[2] * el[3] for el in factor_lst) - Tz * Tn) / N) / (Sz * Sn)
print(f"\nr1,Ri = {rxn}, r2,Ri = {ryn}, r3,Ri = {rzn}")
