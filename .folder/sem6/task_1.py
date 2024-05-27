"""
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком 
они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество 
элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов 
во втором массиве. Затем элементы второго массива
"""

list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]

# lst = list(map(int, input("Input the numbers with space").split()))

# traditional operator using append function
res = []
for elem in list_1:
    if elem not in list_2:
        res.append(elem)
print(res)

# list comprehension
print([elem for elem in list_1 if elem not in list_2])


print(*list(filter(lambda x: x not in list_2, list_1)))