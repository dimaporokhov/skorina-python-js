"""Дан вектор A(n). Все компоненты вектора, которые больше семи, заметить на 7.
Под-считать количество таких компонент с нечетными и четными индексами."""


def create_lst(el_type: type):
    try:
        lst_len = int(input(f"input length of {el_type} list\n"))
        print(f"input {lst_len} int elements of the list")
        lst = [el_type(input()) for _ in range(lst_len)]
        print(f"the source is a list of {el_type} numbers --> ", *lst)
        return lst
    except ValueError:
        print("input should be a number")


def replace_by_7(lst: list) -> None:
    """lab1"""
    try:
        result = {"even": 0, "not_even": 0}
        for i, el in enumerate(lst):
            if el > 7:
                lst[i] = 7
                if i % 2 == 0:
                    result["even"] += 1
                elif i % 2 != 0:
                    result["not_even"] += 1
        print(lst)
        print(result)
    except ValueError:
        print("input should be a number")


if __name__ == '__main__':
    try:
        int_lst = create_lst(int)
        replace_by_7(int_lst)
        float_lst = create_lst(float)
        replace_by_7(float_lst)
    except TypeError:
        print("something went wrong, look above for more info")
