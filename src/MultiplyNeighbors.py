# Задача из лекции №4 где надо вывести всех соседей каждого числа в списке.
# Если поступает 1 число, вывести это число.

# Пока index не станет на 1 меньше, складываем соседей
# текущего индекса[index + 1] + [index - 1]. На последней цифре списка
# складываем первую цифру с предпоследней

a = [int(i) for i in input().split()]
index = 0
for i in a:
    if len(a) == 1:
        print(a[0])
        break
    if index == len(a) - 1:
        print(a[0] + a[-2])
    elif i == a[index]:
        print(a[index - 1] + a[index + 1], end=' ')
        index = index + 1
