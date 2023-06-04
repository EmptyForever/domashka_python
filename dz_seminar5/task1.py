# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def proizvedenie_chisel(num, count):
    if count == 0:
        return 1
    if count == 1:
        return num
    return proizvedenie_chisel(num, count - 1) * num

num1 = int(input("chislo: "))
count1 =  int(input("stepen: "))
powFunct = proizvedenie_chisel(num1, count1)
print(f"{num1} В степени {count1} = {powFunct}")