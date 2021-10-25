from math import sqrt

# вероятность
p = 0.02

# количество людей
N = [100, 200, 500, 200]

# сумма контракта
B = [250, 350, 500, 550]

P = 15000
# премия удержания
P_ = 5000

# предел удержания при перестраховании в рублях
r = 300


################################ до перестрахования
print(f"B(i) --> {B}")

MX = [N[i] * p * B[i] for i in range(len(N))]
print(f"MX(i) --> {MX}")

MS = sum(MX)
print(f"MS --> {MS}")

Q = P/MS - 1
print(f"Q --> {Q}")

Q_ = 2 * Q
print(f"Q* --> {Q_}")

B_after = []

for el in B:
    if r >= el:
        B_after.append(0)
    else:
        B_after.append(el - r)

print(f"B(i)* --> {B_after}")

NMi = [N[i] * B_after[i] for i in range(len(N))]
print(f"NMi* --> {NMi}")

q_ = P_ / ((1 + Q_) * sum(NMi))
print(f"q* --> {q_}")
