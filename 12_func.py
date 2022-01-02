# проверка email
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

lst = list(map(str, input().split()))

new_lst = list(filter(lambda x: re.search(regex,x), lst))

print(*new_lst)