from math import log, exp
from sympy import solve, symbols

prices = {'10-09-2021': 332.75,
          '13-09-2021': 338.98,
          '14-09-2021': 343.34,
          '15-09-2021': 338.5,
          '16-09-2021': 334.5,
          '17-09-2021': 325.7,
          '20-09-2021': 335.3,
          '21-09-2021': 340.59,
          '22-09-2021': 343.47,
          '23-09-2021': 344.29,
          '24-09-2021': 355.19}

prices_extra = {'27-09-2021': 354.07,
                '28-09-2021': 360.88,
                '29-09-2021': 360.81,
                '30-09-2021': 363.25,
                '01-09-2021': 376.06}

# случайные значения
En = [0.523532435, -1.238524874, -0.220835545, 0.789807473, 0.475431534, 0.895547601]

prices_lst = list(prices.values())
prices_extra_lst = list(prices_extra.values())

N = len(prices_lst) - 1


print("hi = ln(S[i+1] / S[i])")
h = [log(prices_lst[i+1] / prices_lst[i]) for i in range(N)]
for i, el in enumerate(h):
    print(f"h{i + 1} --> {round(el, 3)}")
print("\n")
for i in range(N + 1):
    print(f"S{i + 1} --> {prices_lst[i]}")


print(f"\nСлучайные значения --> {En}")

T = sum(h) / N
print(f"\nµ̂ --> {T}")


print("(hi-h̅)*(h(i+1)-h̅)")
cov = 0
try:
    for i in range(len(h)):
        res = (h[i] - T) * (h[i+1] - T)
        cov += res
        print(f"{i + 1} --> {res}")
except IndexError:
    pass


cov = cov / 9
S2 = sum(el**2 - 2*el*T + T**2 for el in h) / (N - 1)
print(f"\ncov --> {cov}")
print(f"S2 --> {S2}\n")


b0, b1 = symbols('b0 b1')
B = solve([b0**2 + b1**2 - S2, b0*b1 - cov])
B0 = [B[0][b0], B[0][b1]]
B1 = [B[3][b0], B[3][b1]]
print(f"\nB0 --> {B0}")
print(f"B1 --> {B1}\n")


hn1 = [T + B0[0] * En[i+1] + B1[0] * En[i] for i in range(len(En) - 1)]
hn2 = [T + B0[1] * En[i+1] + B1[1] * En[i] for i in range(len(En) - 1)]
print(" hn1         hn2")
for i in range(len(hn1)):
    if hn1[i] < 0:
        print(f"{round(hn1[i], 4)}      {round(hn2[i], 4)}")
    else:
        print(f" {round(hn1[i], 4)}      {round(hn2[i], 4)}")

S_extra1 = [exp(hn1[0]) * prices_lst[10]]
S_extra2 = [exp(hn2[0]) * prices_lst[10]]
for i in range(1, len(hn1)):
    s1 = exp(hn1[i]) * S_extra1[i - 1]
    s2 = exp(hn2[i]) * S_extra2[i - 1]
    S_extra1.append(s1)
    S_extra2.append(s2)


print("\nМодельные значения = exp(hn) * S[i-1]")
print(" S1           real        S2")
for i in range(len(hn1)):
    s1_check = abs(S_extra1[i] - prices_extra_lst[i])
    s2_check = abs(S_extra2[i] - prices_extra_lst[i])
    print(f" {round(S_extra1[i], 3)}     "
          f" {prices_extra_lst[i]}     "
          f" {round(S_extra2[i], 3)}   "
          f" {'S1' if s1_check < s2_check else 'S2'} более точно")

print("\nМодельные значения в случае S2 - есть более точные предсказания, так "
      "как в 4 из 5 случаях ближе к реальным значениям")
