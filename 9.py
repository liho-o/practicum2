"""
Герой компьютерной игры "Far Cry Primal" Таккар добыл N быков для одного из племени Урус в K семей.
Если поделить добычу честно между всеми семьями, сколько быков придется отпустить на волю?
"""

n, k = input('Введите n и k\n').split(' ')

answer = int(n) % (int(k))

print(answer)
