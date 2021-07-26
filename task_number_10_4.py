# Задание №4 - сделано
def word_substitution(origin, replaced_word, new_word, amount_replacements) -> str:
    origin = origin.replace(replaced_word, new_word, amount_replacements)
    return origin


print(word_substitution('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
