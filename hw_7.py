# 8_7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, num_1, num_2):
        compl = complex(num_1, num_2)
        self.compl = compl

    def __add__(self, other):
        return self.compl + other.compl

    def __mul__(self, other):
        return self.compl * other.compl


compl_1 = ComplexNum(54, 22)
compl_2 = ComplexNum(3, -4)
print(compl_1 + compl_2)
print(compl_1 * compl_2)
