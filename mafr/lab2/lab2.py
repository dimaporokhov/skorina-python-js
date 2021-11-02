from math import log, exp
from sympy import solve, symbols

prices = {'10-09-2021': [332.75, 327.41, 420.5],
          '13-09-2021': [338.98, 326.48, 570],
          '14-09-2021': [343.34, 333.51, 724.5],
          '15-09-2021': [338.5, 326.99, 664],
          '16-09-2021': [334.5, 329.56, 600.5],
          '17-09-2021': [325.7, 326.92, 551],
          '20-09-2021': [335.3, 323.25, 605],
          '21-09-2021': [340.59, 327.8, 702],
          '22-09-2021': [343.47, 327.02, 801],
          '23-09-2021': [344.29, 325.44, 825],
          '24-09-2021': [355.19, 331.68, 986]}

prices_extra = {'27-09-2021': [354.07, 329.3, 968],
                '28-09-2021': [360.88, 328.43, 992],
                '29-09-2021': [360.8, 340.99, 903.5],
                '30-09-2021': [363.25, 338.48, 987.5],
                '01-09-2021': [376.06, 345.85, 134.5]}

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


S2 = sum(el**2 - 2*el*T + T**2 for el in h) / (N - 1)
print(f"S2 --> {S2}\n")
print((sum(prices_lst) / N))
