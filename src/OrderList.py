# Дан список целых чисел. Требуется переместить все ненулевые
# элементы в левую часть списка, не меняя их порядок,
# а все нули - в правую часть. Порядок ненулевых элементов
# изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.


my_list = [1, 0, 2, 0, 3, 1, 2, 2, 3]
for i in my_list:
    if i == 0:
        my_list.remove(i)
        my_list.append(i)
print(my_list)
