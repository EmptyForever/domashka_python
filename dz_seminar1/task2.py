# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input("Введите число: "))
n3 = num % 10
n2 = num // 10 % 10
n1 = num // 100

print(n1,n2,n3)

print(n1 + n2 + n3)