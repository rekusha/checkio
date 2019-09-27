#def all_the_same(elements):
#    return elements[1:] == elements[:-1]
# это красивее

def all_the_same(elements):
    if len(elements) == 0:
        return True
    else:
        first = elements[0]
        for _ in elements:
            if _ == elements[0]:
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(all_the_same([1, 1, 1]))
    print(all_the_same([1, 2, 1]))
    print(all_the_same(['a', 'a', 'a']))
    print(all_the_same([]))
    print(all_the_same([1]))
    print("Coding complete? Click 'Check' to earn cool rewards!")
