"""Даны два списка чисел. Посчитайте,
сколько чисел содержится
одновременно как в первом списке, так и во втором.
"""

lst_1 = [1, 2, 3, 4, 1]
lst_2 = [2, 3, 5, 2, 3, 7, 4]
lst_1 = set(lst_1)
lst_1.intersection_update(lst_2)
print('Содержится {} чисел одновременно в двух списках'.format(len(lst_1)))
print(lst_1)
