"""
В некоторой компании было подсчитано, что ее ежегодная прибыль, как правило,
составляет 19% от общего объема продаж.
Напишите программу, которая просит пользователя ввести плановую сумму общего объема продаж
и затем показывает прибыль, которая будет получена от этой суммы.

Программа должна выводить в ответе два знака после десятичной точки.
"""

predict_receive = float(input('Ввведите плановую сумму общего объема продаж\n'))

profit = predict_receive * 0.19

print(round(profit, 2))
