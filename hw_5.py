many = int(input("Укажите вашу выручку за последний год, руб.: "))
cost = int(input("Укажите ваши издержки за последний год, руб.: "))
profit = many - cost
rent = profit / many

if profit > 0:
    print(f"Поздравляем, ваша компания приносит {profit} руб. прибыли!")
    print(f"Рентабельность бизнеса составляет {rent}% !")
    members = int(input("Укажите кол-во сотрудников вашей компании: "))
    many_members = profit / members
    print(f"Прибыль фирмы на одного сотрудника составляет {many_members} руб.!")
elif profit == 0:
    print("Ваша компания не убыточная, но прибыли не приносит!")
else:
    print("Ваша компания убыточная! Стоит пересмотреть подход к бизнесу!")
