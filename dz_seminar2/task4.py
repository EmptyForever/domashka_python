
# 2.2[12]
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# сумму этих чисел S и их произведение P. 
# x == ? y == ?

# 1. принимаем от пользователя число S и P
# 2. с помощью математики составляем уравнения. Поулчаем квадратное и приравниваем его к нулю
# 3. находим корни этого уравнения, это возможные иксы 


# S == x + у 
# P == х * у
# множитель в квадратном уравнении. в данной ситуации ни на что не влияет
# Калинкин Алексей
a = 1

S = int(input('Введите число: '))
P = int(input('Введите число: '))

x1 = (S + (S**2 + 4*a*P)**0.5) / 2*a
x2 = (S - (S**2 + 4*a*P)**0.5) / 2*a 

print(x1, x2)

# y = S - x1
# print(x1, y)
