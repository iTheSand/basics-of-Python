# 8_2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_num_1 = int(input("Введите положительное число: "))
inp_num_2 = int(input("Введите положительное число: "))

try:
    res = inp_num_1 / inp_num_2
    if inp_num_2 < 0:
        raise OwnError("Отрицательное число!")
except ZeroDivisionError:
    print("Делить на 0 нельзя!")
except OwnError as err:
    print(f"{err} \nрезультат = {res}")
else:
    print(f"результат = {res}")
