# 5_1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

con = False
str_list = []
while con == False:
    st = input("Введите строку: ")
    str_list.append(st)
    if st == "":
        str_list.remove("")
        con = True

with open("words_hw1.txt", "w", encoding="utf-8") as out_f:
    for el in str_list:
        out_f.write(el)
        out_f.write("\n")
