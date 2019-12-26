import copy
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].


lst1 = [x + y for x in 'ab' for y in 'bcd']
print(lst1)
print(lst1[::2])

# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
# списке этого элемента не было.


lst2 = [i + 'a' for i in '1234']
print(lst2)
print(lst2.pop(1))
print(lst2)
lst3 = copy.deepcopy(lst2)
lst3.append('2a')
lst3.sort()
print(lst3)
