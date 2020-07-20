#main
number = int(input("Введите целое положительное число: "))

last_n = number % 10
number = number // 10

while number > 0:
    if number % 10 > last_n:
        last_n = number % 10
    number = number // 10
print(last_n)

#gb
number = int(input("Введите целое положительное число: "))
great_dig = 0 #текущий максимум
num = number #переменная для оставшейся части числа

while num > 0:
    digit = num % 10 #опр. последнюю цифру
    if digit > great_dig: #сравниваем с текущим максимумом
        great_dig = digit #при необходимости меняем максимум
        if great_dig == 9:
            break
    num = num // 10 #отсекаем от числа последнюю цифру
print(f"Наибольшая цифра в числе {number} равна {great_dig}")