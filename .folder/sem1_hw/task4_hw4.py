"""
Определите, можно ли от шоколадки размером a x b долек отломить c долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
на два прямоугольника).

Выведите yes или no соответственно.
"""

a = int(input("Enter the length of chocolate and amount of tiles: "))
b = int(input("Enter the wide of chocolate: "))
c = int(input("Enter the amount of tiles: "))

if c <= a * b and c % 2 == 0:
    print("yes")
else:
    print("no")