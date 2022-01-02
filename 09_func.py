# числа Фибоначчи
def fibb(n): # рекурсия
    if n == 0:
        return 0
    elif n == 1:
        return  1
    elif n == 2:
        return 1
    else:
        return  fibb(n-1) + fibb(n -2)


def fibb_2(n): # цикл
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2, = f2, f1 + f2
    return f2

if __name__ == '__main__':
    print(fibb(10))
    print(fibb_2(10))