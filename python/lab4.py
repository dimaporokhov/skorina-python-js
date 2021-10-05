"""Написать программу на языке Python,создающую из русско-английского словаря англо-русский словарь
(обязательно использовать словари(dict)).Входные данные берутся из файла input.txt,выходные данные
записываются в файл output.txt.Входные данные лексикографически отсортированы,и выходные данные тоже
должны быть отсортированы! В выходной файл первым записать полученное количество английских слов!
Необходимо, чтобы во входном файле находилось, как минимум, 5 русских слов, которые имеют несколько
английских значений.На хорошую оценку по работе слова должны быть подобраны так, как в моём примере,
чтобы в результате одно английское слово имело несколько русских значений."""


INPUT_FILE = r"D:\skorina-python-js\python\input.txt"
OUTPUT_FILE = r"D:\skorina-python-js\python\output1.txt"


def read_data():
    """read data"""
    with open(INPUT_FILE, encoding="utf-8") as file:
        file.readline()
        r_e_dict = {}
        for line in file:
            key, val = line.split(" - ")
            r_e_dict.update({key: val.replace("\n", "")})
    return r_e_dict


def prepare_data(source_dict: dict) -> dict:
    """prepare data"""
    e_r_dict = {}
    for k, v in source_dict.items():
        for word in v.split(", "):
            e_r_dict[word] = e_r_dict.get(word, ()) + (k,)
    e_r_dict = dict(sorted(e_r_dict.items(), key=lambda x: x[0]))
    return e_r_dict


def write_data(write_dict: dict) -> None:
    """write data"""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.writelines(f"{len(write_dict)}\n")
        for k, v in write_dict.items():
            file.write(f"{k} - {', '.join(word for word in v)}\n")


dict_to_write = prepare_data(read_data())
write_data(dict_to_write)
