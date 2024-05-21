"""
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a 
в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.


"""

def f_1(a,b):
    res = 1
    for _ in range(b):
        res *= a
    return res

a = 3
b = 5
print(f_1(a,b))

def f_2(a,b,res=1):
    if b == 0:
        return res
    return f_2(a, b-1, res * a)

a = 3
b = 5
print(f_2(a,b))



