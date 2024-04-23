"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на 
новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
"""

data  = list(map(int, input("Enter the numbers: ").split()))

max_num = data[0]
min_num = data[0]


for element in data:
    if element > max_num:
        max_num = element
    if element < min_num:
        min_num = element

print(min_num, max_num)


#recursion

def func(data=list(map(int, input("Enter the numbers: ").split())), max_num=data[0], min_num=data[0]):
    if len(data) == 0:
        return  max_num, min_num
    if data[0] > max_num:
        max_num = element
    if data[0] < min_num:
        min_num = element
    return func(data[1:], max_num, min_num)

print(func(data))
