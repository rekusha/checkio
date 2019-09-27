def popular_words(text: str, words: list) -> dict:
    words_dict = {}
    for i in words:
        words_dict.setdefault(i.lower(), 0)
    for word in text.lower().split():
        if word in words_dict:
            words_dict[word] += 1
    return words_dict


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
