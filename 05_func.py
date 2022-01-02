# алгоритм быстрого возведения в степень
def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * pow(a, n-1)
    else:
        return pow(a, n//2)**2

if __name__ == '__main__':
    print(pow(2, 10))