def subgen(n): # подгенератор
    for i in range(n):
        yield i


def delegator(source): # делегирующий генератор
    # for item in source:
    #     yield item
    yield from source


g = subgen(9)

for j in delegator(g):
    print(j)