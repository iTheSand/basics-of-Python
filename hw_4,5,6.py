# 8_4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 8_5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# 8_6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП


class Warehouse:
    def __init__(self, name, count_of_place):
        self.name = name
        self.count_of_place = count_of_place
        print(f"Склад - {self.name}, общее кол-во мест - {self.count_of_place}")

        self.dict_warehouse_1 = {
            "принтер": 5,
            "сканер": 5,
            "ксерокс": 5
        }
        self.dict_warehouse_2 = {
            "Осталось мест на складе": self.count_of_place - (sum(self.dict_warehouse_1.values()))
        }
        print(f"Единиц техники на складе:\n{self.dict_warehouse_1}\n{self.dict_warehouse_2}")

    @property
    def printer(self):
        pass

    @property
    def scan(self):
        pass

    @property
    def xrerox(self):
        pass

    @property
    def data_base(self):
        try:
            self.dict_warehouse_1["принтер"] += self.printer
            self.dict_warehouse_1["сканер"] += self.scan
            self.dict_warehouse_1["ксерокс"] += self.xrerox
        except TypeError:
            print()
            print("Нужно отправить отобранную технику на склад! (transportation)")

        self.dict_warehouse_2 = {
            "Осталось мест на складе": self.count_of_place - (sum(self.dict_warehouse_1.values()))
        }
        print(f"Единиц техники на складе:\n{self.dict_warehouse_1}\n{self.dict_warehouse_2}")
        print()


class OficeEquip():
    def __init__(self, name_of_equip):
        self.name_of_equip = name_of_equip
        print(f"устройство - {self.name_of_equip}")

    def take_away(self, num):
        self.num = num
        print(f"отобрано - {self.num} {self.name_of_equip}")

    def transportation_to_located(self, located):
        self.located = located

    @property
    def transportation(self):
        try:
            if self.name_of_equip == "принтер" and self.located == "склад":
                Warehouse.printer = self.num
            elif self.name_of_equip == "принтер" and self.located != "склад":
                Warehouse.printer = -self.num

            if self.name_of_equip == "сканер" and self.located == "склад":
                Warehouse.scan = self.num
            elif self.name_of_equip == "сканер" and self.located != "склад":
                Warehouse.scan = -self.num

            if self.name_of_equip == "ксерокс" and self.located == "склад":
                Warehouse.xrerox = self.num
            elif self.name_of_equip == "ксерокс" and self.located != "склад":
                Warehouse.xrerox = -self.num
        except AttributeError:
            print("Необходимо указать количество оборудования!")

        if self.located == "склад":
            print(f"отправлено на {self.located}")
            print()
        else:
            print(f"отправлено со склада в {self.located}")
            print()


class Printer(OficeEquip):
    def print(self):
        print("Запущена печать документов")

    def stop_print(self):
        print("Печать документов остановлена")


class Scanner(OficeEquip):
    def scan(self):
        print("Запущено сканирование документов")

    def stop_scan(self):
        print("Cканирование документов остановлено")


class Xerox(OficeEquip):
    def xe(self):
        print("Запущена ксерокопия документов")

    def stop_xe(self):
        print("Ксерокопия документов остановлена")


warehouse_1 = Warehouse("северный", 55)
print()

pr_1 = Printer("принтер")
pr_1.take_away(5)
pr_1.transportation_to_located("склад")
pr_1.transportation

print()
sc_1 = Scanner("сканер")
sc_1.take_away(5)
sc_1.transportation_to_located("склад")
sc_1.transportation

print()
x_1 = Xerox("ксерокс")
x_1.take_away(5)
x_1.transportation_to_located("склад")
x_1.transportation

warehouse_1.data_base

pr_2 = Printer("принтер")
pr_2.take_away(3)
pr_2.transportation_to_located("склад")
pr_2.transportation

sc_2 = Scanner("сканер")
sc_2.take_away(3)
sc_2.transportation_to_located("склад")
sc_2.transportation

x_2 = Xerox("ксерокс")
x_2.take_away(3)
x_2.transportation_to_located("склад")
x_2.transportation

warehouse_1.data_base
