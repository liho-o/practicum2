"""
У Буратино N друзей, с которыми он готов поделиться шоколадными конфетами.
В кульке M конфет. Друзья делят их поровну, то что не делится - остается в кульке.
Сколько конфет достанется каждому (включая Буратино)? В одной строке вводятся два числа N и М через пробел.
"""

n, m = input('Введите n и m\n').split(' ')

answer = int(m) // (int(n)+1)

print(answer)
