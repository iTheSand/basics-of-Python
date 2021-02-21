# 5_7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open("text_7.txt", "r", encoding="utf-8") as f_cool:
    content = f_cool.read()
    content = content.split()

    name = [content[i] for i in range(0, len(content), 4)]
    profit = [int(content[i]) for i in range(2, len(content), 4)]
    cost = [int(content[i]) for i in range(3, len(content), 4)]
    gain = [profit[i] - cost[i] for i in range(0, len(profit))]
    dict_1 = dict(zip(name, gain))

    mid_gain = sum([el for el in gain if el > 0]) / len([el for el in gain if el > 0])
    dict_2 = {"average_profit": mid_gain}

li_result = [dict_1, dict_2]
print(li_result)

with open("my_file_hw7.json", "w", encoding="utf-8") as f_out:
    json.dump(li_result, f_out, indent=4, ensure_ascii=False)
