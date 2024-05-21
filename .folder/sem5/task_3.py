"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
"""

# 2 3 5 7 11

def func_1(n):
    for element in range(2, n):
        if n % element == 0:
            return "no"
    return "yes"

print(func_1(2))



def func_2(n, el=2):
    if el < n:
        if n % el == 0:
            return "no"
        return func_2(n, el+1)
    return "yes"

print(func_2(4))