"""Таможня"""
"""Задание 6. Написать программу на языке Python с использованием декораторов. Должен быть описан один общий декоратор,
который будет использоваться для декорирования нескольких функций (как минимум, двух!) и одного метода класса, также
необходимо написать программу, в которой будет использовано несколько декораторов для одной функции или метода.
Функции и их содержание (например, вывод текста на экран) должны соответствовать заданной предметной области."""


def common_decorator(fun):
    def wrapped(*args):
        print("Я общий декоратор")
        return fun(*args)

    return wrapped


def make_bold(fun):
    def wrapped(*args):
        return fun(*args) + "круто"

    return wrapped


def make_italic(fun):
    def wrapped(*args):
        return fun(*args) + "это "

    return wrapped


def make_underline(fun):
    def wrapped(*args):
        return fun(*args) + " - "

    return wrapped


class A:
    @common_decorator
    @make_bold
    @make_italic
    @make_underline
    def print_data(self):
        return "Таможня"


@common_decorator
@make_bold
@make_italic
@make_underline
def print_data(txt="Таможня"):
    return txt


print(print_data())
print(A().print_data())
