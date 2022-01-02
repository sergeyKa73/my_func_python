def get_nod(a, b):
    """
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while b > 0:
        a, b = b, a % b
    return  a


if __name__ == '__main__':
    print(get_nod(200, 30))