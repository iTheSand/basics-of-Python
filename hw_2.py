# 7_2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def sum_cl(self):
        pass


class Clo(MyAbstractClass):
    def __init__(self, size=100):
        self.size = size

    @property
    def cons_coat(self, v):
        pass

    @property
    def cons_cost(self, h):
        pass

    @property
    def sum_cl(self):
        return f"Общий расход ткани = {self.cons_coat + self.cons_cost} см."


class Coat(Clo):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 40:
            self.__v = 40
        elif v > 60:
            self.__v = 60
        else:
            self.__v = round(v)

    @property
    def sum_cloth_1(self):
        result = round(self.v * 6.5 + 0.5, 1)
        Clo.cons_coat = result
        return f"Расход ткани для пальто {self.name} ({self.v} размера) - {result} см."


class Suit(Clo):
    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 150:
            self.__h = 150
        elif h > 210:
            self.__h = 210
        else:
            self.__h = round(h)

    @property
    def sum_cloth_2(self):
        result = round((self.h) * 2 + 0.3, 1)
        Clo.cons_cost = result
        return f"Расход ткани для костюма {self.name} (на рост {self.h} см.) - {result} см."


clo_1 = Clo()
clo_2 = Coat("DG", 39)
print(clo_2.sum_cloth_1)
print()
clo_3 = Suit("Qwerty", 163.9)
print(clo_3.sum_cloth_2)
print()
print(clo_1.sum_cl)
