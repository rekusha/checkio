VOWELS = "aeiouy"

def translate(phrase):
    result = []
    i = 0
    while True:
        result.append(phrase[i])
        if phrase[i] in VOWELS:
            i+=3
        elif phrase[i] == ' ':
            i+=1
        else:
            i+=2
        if i >= len(phrase):
            break
    return ''.join(str(_) for _ in result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    translate("hieeelalaooo")
    translate("hoooowe yyyooouuu duoooiiine")
    translate("aaa bo cy da eee fe")
    translate("sooooso aaaaaaaaa")
