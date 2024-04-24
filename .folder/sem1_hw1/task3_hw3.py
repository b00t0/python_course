"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран 
yes или no."""

n = int(input("Enter the six digit number: "))

number1 = n // 1000
number2 = n % 1000

sum1 = int(number1 // 100 + number1 // 10 % 10 + number1 % 10)
# print(sum1)

sum2 = int(number2 // 100 + number2 // 10 % 10 + number2 % 10)
# print(sum2)

if sum1 == sum2:
    print("yes")
else:
    print("no")