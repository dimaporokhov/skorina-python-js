"""Вариант 15
Разработать программу, присваивающую некоторой переменной значение "истина",
если букв латинского алфавита во введенном тексте больше строчных гласных букв русского алфавита
 и значение ложь в противном случае. Подсчитать количество цифр. На печать выдать исходный текст,
 значение логической переменной и количество цифр.
"""

ENGLISH = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
RUSSIAN_VOWELS = list("АЕЁИОУЫЭЮЯаеёиоуыэюя")

string = input("Please input source string\n")
digits_amount = len([el for el in string if el.isdigit()])
english_amount = len([el for el in string if el in ENGLISH])
russian_vowels_amount = len([el for el in string if el in RUSSIAN_VOWELS])
bool_var = english_amount > russian_vowels_amount
print(f"source: {string}\n",
      f"\benglish letters are more than russian vowels is {bool_var}\n",
      f"\bamount of digits is {digits_amount}")

