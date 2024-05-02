# change the first and the last elements

array = [34, 545, 65, 7, 65, 6]

last =  array.pop()
first = array.pop(0)

array.insert(0, last)
array.append(first)

print(array)