"""Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию)."""

a = int(input('Введите 1 число'))
b = int(input('Введите 2 число'))
while a and b:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a or b)
