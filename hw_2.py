time_s = int (input("Введите время в секундах: "))

hours = time_s // 3600
part_h = time_s % 3600
minute = part_h // 60
second = part_h % 60

if hours < 10:
    hours = f"0{hours}"
if minute < 10:
    minute = f"0{minute}"
if second < 10:
    second = f"0{second}"

print(f"{hours}:{minute}:{second}")

