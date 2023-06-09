# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

# a.intersection(b)
# так как нам не важны повторения, то мы можем взять этот списки и сформировтаь из них множества
# с множества есть много варианто взаимодейстия. в данной ситуации нам нужны пересечения. тое сть чиса встречающиеся и там и там
# a.intersection(b)   

list_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
list_2 = [3, 6, 12, 9, 15, 18]
set1 = set(list_1)
set2 = set(list_2)
print(set1, set2)
peresech1_2 = list(set1.intersection(set2))
if peresech1_2 == []:
    print("net peresecheni")
else:
    peresech1_2.sort()
    print(*peresech1_2)