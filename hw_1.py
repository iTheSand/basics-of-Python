# 8_1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    def __str__(self):
        return f"Текущая дата: {self.day_month_year}"

    @classmethod
    def my_cls(cls, day_month_year):
        my_date = [int(el) for el in day_month_year.split("-")]
        return f"Текущая дата: {my_date[0]} день {my_date[1]} месяц {my_date[2]} год"

    @staticmethod
    def my_valid(day_month_year):
        my_date = [int(el) for el in day_month_year.split("-")]
        if my_date[0] <= 31 and my_date[1] <= 12 and my_date[2] <= 2020:
            print("Корректная дата!")
        else:
            print("Введена не корректная дата! Проверьте день, месяц и год!")

date_1 = Date("06-06-2006")
print(date_1)
print(Date.my_cls("06-06-2006"))
Date.my_valid("20-12-2006")
