# -*- coding: utf-8 -*-

# Anagrams

# This script reverses all the words of input text:
# E.g. "abcd efgh" => "dcba hgfe"
# All non-letters symbols stays on the same places:
# E.g. "a1bcd efg!h => "d1cba hgf!e"
# Use Latin alphabet for use only


def revers_words(string_words):
    list_words = string_words.split()
    for index, word in enumerate(list_words):
        if word.isalpha():
            list_words[index] = ''.join(reversed(word))
            # list_words[index] = word[::-1}
        else:
            word = list(word)
            symbols_dict = {}
            word_copy = word.copy()
            for char in word_copy:
                if not char.isalpha():
                    symbols_dict[char] = word_copy.index(char)
                    word.remove(char)
            word.reverse()
            for key, value in symbols_dict.items():
                word.insert(value, key)
            word = ''.join(word)
            list_words[index] = word
    return ' '.join(list_words)


words_for_invert = revers_words("kuh6g84tg liji8ggh")
print(words_for_invert)
