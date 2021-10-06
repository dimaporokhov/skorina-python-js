"""15.	Создать новый текст, содержащий все слова исходного текста, которые окан-чиваются на ту же букву,
что и слово максимальной длины. Из исходного текста эти сло-ва удалить."""

string = input("input string\n")
temp = string


sep_set = {sep for sep in string if not sep.isalpha() and not sep.isdigit() and sep != ' '}
for sep in sep_set:
    temp = temp.replace(sep, ' ')
words = [word for word in temp.split(' ') if word != '']


max_word_lst = ['']
for word in words:
    if len(word) == len(max_word_lst[0]):
        max_word_lst.append(word)
    if len(word) > len(max_word_lst[0]):
        max_word_lst = [word]


filter_letters = ''.join(word[-1] for word in max_word_lst)
new_str = ' '.join(word for word in words if word[-1] in filter_letters)


delete_words = new_str.split(' ')
for word in delete_words:
    string = string.replace(word, ' ')

print(new_str)
print(string)
