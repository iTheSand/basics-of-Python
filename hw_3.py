# 3_3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(s_1, s_2, s_3):
    li = [s_1, s_2, s_3]
    li.sort()
    print(li[1] + li[2])


my_func(3, 100, 20)
