"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

"""

var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

# n, m = map(int, (input("Enter the amount of var2 and var3: ").split()))

# print(f"The amount of var2 and var3: {n}, {m}")

# new_var2 = []
# new_var3 = []

# def enter_the_list(l):
#     new_list = []
#     for _ in range(l):
#         number = int(input(f"Enter the numbers for var: "))
#         new_list.append(number)
#     return new_list

# new_var2 = enter_the_list(n)
# # set_var2 = set(new_var2)
# print("var2: ", new_var2)
# new_var3 = enter_the_list(m)
# # set_var3 = set(new_var3)
# print("var3: ", new_var3)

result = list(set(map(int,var2.split())) & set(map(int,var3.split())))
result.sort()
print(*result)
