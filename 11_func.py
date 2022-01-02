def triangle_pascal(n):
    p= []
    for i in range(n+1):
        row = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = p[i-1][j-1] + p[i-1][j]
        p.append(row)
    return p
if __name__ == '__main__':
    n = int(input('Enter number: '))
    r = triangle_pascal(n)
    for i in r:
        print(i)
