# 2_2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = []

answer = ""

while True:
    if answer == "нет":
        break
    enter = input("Введите элемент списка: ")
    list.append(enter)
    if len(list) >= 3:
        answer = input("Продолжить заполнять список (да, нет)? ")
        if answer == "да":
            continue
        elif answer == "нет":
            break
        else:
            while True:
                print("Введите корректный ответ (да, нет)!")
                answer = input("Продолжить заполнять список (да, нет)? ")
                if answer == "да":
                    break
                elif answer == "нет":
                    break

print(f"сформированный список list = {list}")

k = 0
for i in range(int(len(list) / 2)):
    list[k], list[k + 1] = list[k + 1], list[k]
    k += 2

print(f"список с замененными соседними элементами {list}")
