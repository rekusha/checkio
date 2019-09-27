def flat_list(array):
    result = []
    def temp(x):
        for i in x:
            if isinstance(i, int):
                result.append(i)
            else:
                temp(i)
    temp(array)
    return result

if __name__ == '__main__':
    flat_list([1, 2, 3])
    flat_list([1, [2, 2, 2], 4])
    flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])
    flat_list([-1, [1, [-2], 1], -1])
    print('Done! Check it')
