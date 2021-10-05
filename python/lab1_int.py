"""Дан вектор A(n). Все компоненты вектора, которые больше семи, заметить на 7.
Под-считать количество таких компонент с нечетными и четными индексами."""

try:
    LST_LEN = int(input("input the length of int list\n"))
    print(f"input {LST_LEN} int elements to create a list")

    lst = [int(input()) for _ in range(LST_LEN)]
    print("the source is a list of int numbers --> ", *lst)

    result = {"even": 0, "not_even": 0}
    for i, el in enumerate(lst):
        if el > 7:
            lst[i] = 7
            if i % 2 == 0:
                result["even"] += 1
            elif i % 2 != 0:
                result["not_even"] += 1

    print(f"result list --> {lst}")
    print(f"amount of even indices which element is more than 7 --> {result['even']}")
    print(f"amount of not even indices which element is more than 7 --> {result['not_even']}")
except ValueError:
    print("input should be a valid int number, not a string or float")
