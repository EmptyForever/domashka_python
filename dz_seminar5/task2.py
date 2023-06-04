# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

# операции --> +1       -1
# циклы нельзя.
#       то бишь условия то наверное можно)))
# базис рекурсии и погнали
def summNum(number1, number2):
    if number1 == 0 and number2 == 0:
        return 0
    if number1 == 0:
        return 1 + summNum(number1, number2 -1)
    if number2 == 0:
        return 1 + summNum(number1 - 1, number2)
    return 1 + 1 + summNum(number1 - 1, number2 - 1)

print(summNum(0, 3))