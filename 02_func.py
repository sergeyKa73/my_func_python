#Сортировка вставками

a = [-3, 5, 0, -8, 1, 10]
n = len(a) # число элементов в списке

for i in range(1, n):
    for j in range(i, 0, -1 ):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break


if __name__ == '__main__':
    print(a)