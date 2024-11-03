# TODO реализовать функцию
def get_unique_words(word):
    a = list(set(word.split()))



    a.sort()
    return a



print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
