def count_consecutive_summers(num):
    res_list = []
    for i in range(1, num+1):
        temp = 0
        for _ in range(i, num+1):
            temp += _
            if temp == num:
                res_list.append(temp)
            elif temp > num:
                break
    return len(res_list)


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
