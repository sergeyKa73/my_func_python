#  функция слияния двух отсортированных списков:
def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


# функция деления списка и слияния в общий отсортированный  список
def split_and_merge_list(a):
    N1 = len(a) // 2 # деление массива на два примерно равной длины
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:  # если длина 1-го списка больше 1, то делим дальше
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:  # если длина 2-го списка больше 1, то делим дальше
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)  # слияние двух отсортированных списков

if __name__ == '__main__':
    a = list(map(int, input().split()))
    a = split_and_merge_list(a)

    print(*a)