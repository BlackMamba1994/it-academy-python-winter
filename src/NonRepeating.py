# Вводится строка.Требуется удалить из нее повторяющиеся символы и все пробелы
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

# суммируем в новую переменную каждую новую
# букву. Пробелы сразу заменяем
a = input()
c = ''
a = a.replace(' ', '')
for i in a:
    if i not in c:
        c += i
print(c)
