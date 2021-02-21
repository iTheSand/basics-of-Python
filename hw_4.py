# 6_4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Машина {self.color} цвета, марки {self.name}")
        if self.is_police == True:
            print("Принадлежит полиции!")

    def go(self):
        li = ["Москва-Сити", "Красная площадь", "Новая Москва", "м. Таганская", "м. Фрунзенская", "м. Киевская"]
        print(f"Начала движение в районе {choice(li)}")

    def stop(self):
        li = ["Москва-Сити", "Красная площадь", "Новая Москва", "м. Таганская", "м. Фрунзенская", "м. Киевская"]
        print(f"Остановилась в районе {choice(li)}")

    def turn(self):
        li = ["север", "юг", "запад", "восток"]
        print(f"Повернула на {choice(li)}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость {self.speed} км/ч - превышение!")
        else:
            print(f"Текущая скорость - {self.speed} км/ч")


class SportCar(Car):
    def show_speed(self):
        print("Камеры не определяют скорость из-за большого превышения!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.speed} км/ч - превышение!")
        else:
            print(f"Текущая скорость - {self.speed} км/ч")


class PoliceCar(Car):
    def go(self):
        print("Информация о местоположении недоступна")

    def stop(self):
        print("Информация о местоположении недоступна")

    def turn(self):
        print("Информация о местоположении недоступна")

    def show_speed(self):
        print("Информация о скорости недоступна")


car_1 = TownCar(61, "красного", "Nissan")
car_1.go(), car_1.turn(), car_1.show_speed(), car_1.stop()
print()

car_2 = TownCar(59, "черного", "BMW")
car_2.go(), car_2.turn(), car_2.show_speed()
print()

car_3 = SportCar(120, "синего", "Tesla")
car_3.go(), car_3.turn(), car_3.show_speed()
print()

car_4 = WorkCar(45, "черного", "Зил")
car_4.go(), car_4.turn(), car_4.show_speed(), car_4.stop()
print()

car_5 = PoliceCar(60, "белого", "Skoda", True)
car_5.go(), car_5.turn(), car_5.show_speed(), car_5.stop()
