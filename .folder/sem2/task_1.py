"""
По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N
 (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

"""
#while

number = int(input("Enter the number: "))
f = 1

while number > 1:
    f *= number
    number -= 1

print(f)


#for

for element in range(1, number + 1):
    f *= element

print(f)

# recursion

def factorial(num, f = 1):
    if num == 0:
        return f
    return factorial(num - 1, f * num)

print(factorial(5))