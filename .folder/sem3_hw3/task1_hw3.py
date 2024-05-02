"""
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

Найдите количество и выведите его.


"""

# user input

# list_1 = []

# for i in range(int(input('Enter the list size: '))):
#     list_1.append(int(input(f'Enter the {i+1} number: ')))

# print(list_1)

list_1 = [int(input(f'Enter the {i+1} number: ')) for i in range(int(input('Enter the list size: ')))]

print(list_1)

k = int(input('Enter the desired number: '))

# list_1 = [1, 2, 3, 4, 5]

# k = 3

count = 0

for element in list_1:
    if k == element:
        count += 1

print(count)

