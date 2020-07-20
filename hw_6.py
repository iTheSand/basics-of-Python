#main
run_distans_min = int (input("Какое кол-во км. вы пробежали на первой тренировке? "))
run_distans_max = int (input("К какому кол-ву км. вы стремитесь? "))

a = run_distans_min * 1.1
i = 2
while a < run_distans_max:
    a = a * 1.1
    i += 1
print(f"Желаемую дистанцию в {run_distans_max} км. вы пробежите на {i} тренировке!")

#gb
while True:
    i_days = 1 #счетчик дней
    run_distans_min = int (input("Какое кол-во км. вы пробежали на первой тренировке? "))
    run_distans_max = int (input("К какому кол-ву км. вы стремитесь? "))
    if run_distans_min < 0 or run_distans_max < 0:
        print("Введите положительные значения!")
    else:
        while run_distans_min < run_distans_max:
            i_days += 1
            run_distans_min = run_distans_min * 1.1

        print(f"Желаемую дистанцию в {run_distans_max} км. вы пробежите на {i_days} тренировке!")
        break

