# 5. Уникальные элементы в списке
# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.


my_list = [12, 12, 13, 'abc', 'abc', 'zxc']
for i in my_list:
    if my_list.count(i) == 1:
        print(i)