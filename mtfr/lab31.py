from math import sqrt

# вероятность
p = 0.002

# количество людей
N = [12000, 5000, 1000, 2000]

# сумма контракта
B = [100000, 200000, 400000, 500000]

# относительная страховая надбавка
Q = 0.23

# предел удержания при перестраховании в рублях
r = 300000

Q_ = 0.33

################################ до перестрахования
print(f"B(i) --> {B}")

MX = [N[i] * p * B[i] for i in range(len(N))]
print(f"MX(i) --> {MX}")

MS = sum(MX)
print(f"MS --> {MS}")

DX_gr = [N[i] * (p * B[i]**2 - (p * B[i])**2) for i in range(len(N))]
print(f"DX(i) --> {DX_gr}")

U = (1 + Q) * MS
print(f"U --> {U}")

I = U - MS
print(f"I --> {I}")

DS = sum(DX_gr)
print(f"DS --> {DS}")
R = f"1 - N({I / sqrt(DS)})"
print(f"R --> {R}")

################################ после перестрахования
B_after = []
i_after = []
for i, el in enumerate(B):
    if el > r:
        B_after.append(el - r)
        i_after.append(i)
    else:
        B_after.append(el)
print(f"\nB(i)* --> {B_after}")

MX_after = [N[i] * p * B_after[i] for i in range(len(N))]
print(f"MX(i)* --> {MX_after}")

MS_after = sum(MX_after)
print(f"MS* --> {MS_after}")

DX_gr_after = [N[i] * (p * B_after[i]**2 - (p * B_after[i])**2) for i in range(len(N))]
print(f"DX(i)* --> {DX_gr_after}")

P_ = (1 + Q_) * (MS - MS_after)
print(f"P* --> {P_}")

U_ = U - P_
print(f"U* --> {U_}")

I_ = U_ - MS_after
print(f"I* --> {I_}")

DS_after = sum(DX_gr_after)
print(f"DS* --> {DS_after}")
R_ = f"1 - N({I_ / sqrt(DS_after)})"
print(f"R* --> {R_}")
