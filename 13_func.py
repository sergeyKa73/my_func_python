# поиск в словаре по ключу
def recurs_find_key(key, obj):
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if type(v) == dict:
            result = recurs_find_key(key, v)
            if result is not None:
                return  result
        elif type(v) == list:
            for i in v:
                result = recurs_find_key(key, i)
                if result is not None:
                    return result


if __name__ == '__main__':
    pass