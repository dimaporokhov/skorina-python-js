from math import log, sqrt, e

prices = {'10-09-2021': 326.43,
          '13-09-2021': 331.0,
          '14-09-2021': 339.0,
          '15-09-2021': 342.6,
          '16-09-2021': 339.41,
          '17-09-2021': 334.5,
          '20-09-2021': 326.32,
          '21-09-2021': 334,
          '22-09-2021': 338.99,
          '23-09-2021': 343.47,
          '24-09-2021': 344.29,
          '27-09-2021': 351.05,
          '28-09-2021': 356.67,
          '29-09-2021': 358.5,
          '30-09-2021': 361.54,
          '01-10-2021': 363.25}

prices_lst = list(prices.values())

N = 10
h = [log(prices_lst[i] / prices_lst[i+1]) for i in range(N)]

print("hi = ln(S[i+1] / S[i])")
for i, el in enumerate(h):
    print(f"h{i + 1} --> {el}")
print("\n")
for i, el in enumerate(prices_lst):
    print(f"S{i + 1} --> {el}")

T = sum(h) / N
S2 = sum(el**2 - 2*el*T + T**2 for el in h) / (N - 1)
S = sqrt(S2)

En = [0.523532435, -1.238524874, -0.220835545, 0.789807473, 0.475431534]

h_extra = [T + S * el for el in En]
S_extra = [e**h_extra[0] * prices_lst[-1]]
for i in range(1, 5):
    s = e**h_extra[i] * S_extra[i - 1]
    S_extra.append(s)

print(f"\nT --> {T}")
print(f"S --> {S}\n")

print("h[i] extra = T + S * En")
for i, el in enumerate(h_extra):
    print(f"h1{i + 1} --> {el}")
print("\nS[i] extra = e^h[i] * S[i-1]")
for i, el in enumerate(S_extra):
    print(f"S1{i + 1} --> {el}")
print("Спрогнозированные значения довольно выгодные, и практически во всех случаях выгоднее, чем реальные")