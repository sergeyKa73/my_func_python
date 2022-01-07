def create_2d_arr(n, m):
    arr_2d = []
    for i in range(n):
        line =[]
        for i in range(m):
            line.append(0)
        arr_2d.append(line)
    return arr_2d

def print_2d_arr(arr_2d):
    for i in arr_2d:
        print(*i)

arr = create_2d_arr(5, 4)

if __name__ == '__main__':
    print_2d_arr(arr)
