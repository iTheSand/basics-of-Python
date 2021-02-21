# 5_5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

num = []
result = 0

for el in range(30):
    num.append(str(randint(1, 777)))

with open("num_hw5.txt", "w", encoding="utf-8") as f_cool:
    for el in num:
        f_cool.write(el + " ")

with open("num_hw5.txt", "r", encoding="utf-8") as f_out:
    for el in f_out:
        li = el.split()
        for i in li:
            result += int(i)

print(result)
