# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]

print(len(set(list_1)))

# another way

list_2 = []

for element in list_1:
    if element not in list_2:
        list_2.append(element)

print(len(list_2))


