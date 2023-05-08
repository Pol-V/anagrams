def make_anagrams(text_origin):
    if type(text_origin) != str:
        raise TypeError('Please use just strings')
    try:
        if text_origin != ' ':
            text_reversed = []
            for words in text_origin.split():
                word = list(words)
                changing_index = 0
                word_mirror = list(filter(lambda x: x.isalpha(), word[::-1]))
                for index_of_symbol in range(len(word)):
                    if word[index_of_symbol].isalpha():
                        word[index_of_symbol] = word_mirror[changing_index]
                        changing_index += 1
                text_reversed.append(''.join(word))
            return ' '.join(text_reversed)
        else:
            return text_origin
    except TypeError:
        raise TypeError('Please use just strings')
