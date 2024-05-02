"""
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

array = [1, 2, 3, 4, 5]
k = 3
print(array[k:] + array[:k])


# another way

for _ in range(k-1):
    last = array.pop()
    array.insert(0, last)

print(array)