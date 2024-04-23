"""
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель 
за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись
 исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
 Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
   Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50
"""

n = 6
numbers = "-20 30 -40 50 10 -10".split()

max_length = 0
current_length = 0

for element in numbers:
    num = int(element)
    if num > 0:
        current_length += 1
    else:
        current_length = 0
    
    if current_length > max_length:
        max_length = current_length

print(max_length)


#recursion

def func(n, numbers = "-20 30 -40 50 10 -10".split(), max_length = 0, current_length = 0):
    if len(numbers) == 0:
        return max_length
    num = int(numbers[0])
    if num > 0:
        current_length += 1
    else:
        current_length = 0
    
    if current_length > max_length:
        max_length = current_length
    return func(n, numbers[1:], max_length, current_length)

print(func(6))
