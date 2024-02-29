"""
Измените решение для Задания 12 (Практическая работа №1);
таким образом, чтобы программа выводила только значение в рублях (без копеек).
"""

total_coast = input("Значение общей стоимости часов:")
total_coast = float(total_coast)
silv_count = 96
gold_count = silv_count/16
silv_coast = 48

gold_coast = (total_coast - (silv_coast * silv_count))/ gold_count
print(round(gold_coast))