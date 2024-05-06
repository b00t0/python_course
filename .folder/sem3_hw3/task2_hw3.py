"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

Пример:


list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""

# list_1 = [1, 2, 3, 4, 5]
# k = 6
element = 0

list_1 = [int(input(f'Enter the {i+1} number: ')) for i in range(int(input('Enter the list size: ')))]

print(list_1)

k = int(input('Enter the desired number: '))

for i in range(0, len(list_1)):
    if list_1[i] == k:
        element = k
    elif abs(list_1[i]-k) < abs(list_1[len(list_1)-1-i]-k) and abs(list_1[i]-k) < abs(element - k):
        element = list_1[i]

print(element)
