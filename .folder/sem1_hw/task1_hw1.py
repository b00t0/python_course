"""
Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res.

"""

n = int(input("Enter the number: "))

res = 0
while n > 0:
   
    res = res + n % 10
    n = n // 10

print(f"Sum of digits is {res}")