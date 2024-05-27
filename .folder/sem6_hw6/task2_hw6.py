"""
Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и 
количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: 
an = a1 + (n-1) * d.
"""
a1 = 2
d = 3
n = 4

#classic
lst_1 = []
for n in range(1, n+1):
    elem = a1 + (n-1) * d
    lst_1.append(elem)

print(*lst_1, sep = '\n')

#function
def ar_progression(first_number,dif,amount):
    lst_1 = []
    for amount in range(1, amount+1):
        elem = first_number + (amount-1) * dif
        lst_1.append(elem)
    return lst_1

print(*ar_progression(a1,d,n), sep = '\n')
