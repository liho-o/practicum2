"""
Напишите программу, которая вычисляет объем дождя в литрах,
выпавшего на один гектар, если уровень осадков 1 сантиметр.
Программа должна выводить одно число.

Количество осадков в миллиметрах численно равно количеству килограмм воды на метр квадратный (1 мм = 1 кг/м кв)
"""

# a_sm = float(input())

a_sm = 1


a_mm = a_sm * 10

litr_on_ga = a_mm / 10000

print(litr_on_ga)
