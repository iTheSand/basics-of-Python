# 5_4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

translator = Translator()
li = []

with open("text_4.txt", "r", encoding="utf-8") as f_cool:
    for el in f_cool:
        trans = translator.translate(el, src="en", dest="ru")
        li.append(trans.text)

with open("trans_hw4.txt", "w", encoding="utf-8") as f_out:
    for el in li:
        f_out.write(el)
        f_out.write("\n")
