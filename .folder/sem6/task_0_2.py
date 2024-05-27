"""
Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными
кодами Unicode каждого символа введеннной строки отсортированный по убыванию.
"""

def func(data):
    return sorted(set([ord(el) for el in data]), reverse=True)

print(func("abrakadabra"))