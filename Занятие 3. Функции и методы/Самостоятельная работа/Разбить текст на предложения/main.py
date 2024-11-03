# TODO реализовать функцию
def get_sentences_list(str_):
    sentences_list = []
    for sentence in str_.split("."):
        if sentence:
            sentences_list.append(sentence.strip())


    return sentences_list

print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
