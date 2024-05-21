"""
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
"""

"""
0 1 1 2 3 5 8 13 21
"""

n = 7
fibo_p, fibo_n = 0, 1

for _ in range(n):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(fibo_n)



def func(n,fibo_p=0,fibo_n=1):
    if n == 0:
        return fibo_n
    return func(n-1,fibo_n, fibo_p + fibo_n)

print(func(n))