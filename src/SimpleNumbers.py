# 2 Решения задачи на простое число или нет

# Решение через добавление в список всех цифр в список, и
# длина списка больше 2-ух, то число непростое
a = int(input('Введите число '))
i = 0
c = []
while i != a:
    i = i + 1
    if a % i == 0:
        c.append(i)
if len(c) > 2:
    print('Не такое уже и простое число')
else:
    print('Простое число')

# c- число куда суммируются все делители
a = int(input('Введите число '))
c = 0
for i in range(1, a+1):
    if a % i == 0:
        c = c + i
if c == a + 1:
    print('Простое')
else:
    print('Не совсем простое')
