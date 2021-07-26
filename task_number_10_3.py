# Задание №3 - сделано
# Вариант №1
def longest_word(text):
    text = text.split()
    text = max(text, key=len)
    return text


print(longest_word('What makes a good man'))
# Вариант №2


def longest_word_2(text):
    word = ''
    for i in text.split():
        if len(i) > len(word):
            word = i
    return word


print(longest_word_2('What makes a good man'))
