def long_repeat(line):
    max_value = 0
    value = 1
    if len(line) > 0:
        max_value = 1
    for i in range(len(line)):
        if i > 0:
            if line[i] == line[i-1]:
                value += 1
                if value > max_value:
                    max_value = value
            else:
                value = 1
    return max_value

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    long_repeat('sdsffffse')
    long_repeat('ddvvrwwwrggg')
    long_repeat('abababaab')
    long_repeat('')
    print('"Run" is good. How is "Check"?')
