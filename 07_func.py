from string import punctuation

def remove_punctuation(word):
    '''
    функция для удаления знаков пунктуации
    :param word: с
    :return: слово без знаков препинания
    '''
    for p in punctuation:
        if p in word:
            word = word.replace(p , "")
    return word

