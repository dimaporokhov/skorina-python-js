from math import log, exp, sqrt
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
En = [0.523532435, -1.238524874, -0.220835545, 0.789807473, 0.475431534]

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


sum_hi = sum(h[i] for i in range(1, len(h)))
sum_hi_1 = sum(h[i] for i in range(len(h) - 1))
sum_hi_1_2 = sum_hi_1**2
sum_hi_hi_1 = sum(h[i] * h[i - 1] for i in range(1, len(h)))

print(f"\n∑hi --> {sum_hi}")
print(f"∑hi - 1 --> {sum_hi_1}")
print(f"(∑hi - 1)^2 --> {sum_hi_1_2}")
print(f"∑hi * hi - 1 --> {sum_hi_hi_1}")


T = sum(h) / N
S2 = sum(el**2 - 2*el*T + T**2 for el in h) / (N - 1)
S = sqrt(S2)
print(f"\nµ̂ --> {T}")
print(f"S2 --> {S2}")
print(f"σ̂ --> {S}")

a0, a1 = symbols('a0 a1')
A = solve([sum_hi - 4*a0 - sum_hi_1,
           -sum_hi_hi_1 + a0 * sum_hi_1 + a1 * sum_hi_1_2
           ])
print(f"\n{A}")


hn = [A[a0] + A[a1] * h[-1] + S * En[0]]
for i in range(1, len(En)):
    res = A[a0] + A[a1] * hn[i - 1] + S * En[i]
    hn.append(res)

print("\nhn")
for i in range(len(hn)):
    print(f"{round(hn[i], 4)}")


S_extra = [exp(hn[0]) * prices_lst[10]]
for i in range(1, 5):
    s = exp(hn[i]) * S_extra[i - 1]
    S_extra.append(s)

print("\nS")
print("model     real")
for i in range(len(hn)):
    print(f"{round(S_extra[i], 2)}    "
          f"{prices_extra_lst[i]}    "
          f"{'model' if S_extra[i] < prices_extra_lst[i] else 'real'}")


print("Модельные значения довольно выгодные, и в 4 из 5 случаях выгоднее, чем реальные,"
      " но это плохо бы сказалось на компании")
