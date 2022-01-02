# Сортировка выбором

a = [ -3, 5, 0, -8, 1, 10, -67, 32, -7, 42]
n = len(a) # число элементов в списке

for i in range(n-1):
    m = a[i] # min значение
    p = i # инжекс минимального значения
    for j in range(i + 1, n): # поиск min
        if m > a[j]:
            m = a[j]
            p = j
    if p !=i: # обмен значениями
        t = a[i]
        a[i] = a[p]
        a[p] = t

if __name__ == '__main__':
    print(a)