
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.


n = int(input("Enter natural integer number: "))


degree = 1

while degree <= n:
    print(degree)
    degree = degree * 2


#recursion

def func(n, degree):
    if degree > n-1:
        return degree
    print(degree)
    return func(n, degree*2)

print(func(n, 1))