"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает
две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные
Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны 
вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
"""




s = int(input("Enter the sum of X and Y: "))
p = int(input("Enter the product of X and Y: "))

for x in range(s):
    for y in range(s):
        if x <= y:
            if x + y == s and x * y == p:
                print(x, y, "", end='')