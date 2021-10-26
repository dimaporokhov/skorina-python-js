from math import log, sqrt, exp

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
                '29-09-2021': 360.8,
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

T = sum(h) / N
S2 = sum(el**2 - 2*el*T + T**2 for el in h) / (N - 1)
S = sqrt(S2)

print(f"\nµ̂ --> {T}")
print(f"S2 --> {S2}")
print(f"S --> {S}\n")

h_extra = [T + S * el for el in En]
S_extra = [exp(h_extra[0]) * prices_lst[10]]
for i in range(1, 5):
    s = exp(h_extra[i]) * S_extra[i - 1]
    S_extra.append(s)


print("hn = T + S * En")
print(f"Случайные значения En --> {En}")
print("Модельные значения = exp(hn) * S[i-1]\n")

for i in range(len(h_extra)):
    print(f"h1{i + 1} --> {round(h_extra[i], 3)}")
    print(f"S1{i + 1} --> model = {round(S_extra[i], 2)}  real = {prices_extra_lst[i]}")
print("Модельные значения довольно выгодные, и в 3 из 5 случаях выгоднее, чем реальные")
