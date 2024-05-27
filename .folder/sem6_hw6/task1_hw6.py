"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
"""

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

#classic
res = []
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        res.append(i)
print(*res, sep = '\n')


#function
def index_limits(lst,min,max):
    res = []
    for i in range(len(list_1)):
        if min <= lst[i] <= max:
            res.append(i)
    return res

print(*index_limits(list_1,min_number,max_number),sep = '\n')



