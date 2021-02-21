# 6_5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"пишем {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"пишем ручкой - {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"пишем карандашом - {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"пишем маркером - {self.title}")


sta_1 = Stationery("пером")
sta_1.draw()

sta_2 = Pen("Qwe")
sta_2.draw()

sta_3 = Pencil("Зори")
sta_3.draw()

sta_4 = Handle("Fat")
sta_4.draw()
