# Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

list_1 = []   #[10, 5, 7, 3, 3, 7, 5, 7, 2, 8]
print(list_1)

print('ЗАДАЁМ списочек!')
size = int(input('Задайте размер списка: '))
for item in range(size):
    x = int(input(f'Введите число {item + 1}: '))
    list_1.append(x)
print(list_1)

# находим число
x = int(input('Введите искомое число: '))
count = 0

for item in range(len(list_1)):
    if list_1[item] == x:
        count += 1

print('-1') if count == 0 else print('количество вхождений', count)
print(f'функция ".count" выводит количество вхождений числа X в список \n колличество --> {list_1.count(x)}')

# if count == 0: 
#     print('-1')
# else:
#     print(count)





