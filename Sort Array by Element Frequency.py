import operator
def frequency_sort(items):
    work_dict = {}
    work_list = []
    end_list = []
    if items:
        for _ in items:
            if _ in work_dict:
                work_dict[_] += 1
            else:
                work_dict[_] = 1
                work_list.append(_)
        max_count=max(work_dict.items(), key=operator.itemgetter(1))[1]
        while max_count >= 0:
            for i in work_list:
                if work_dict[i] == max_count:
                    for x in range(max_count):
                        end_list.append(i)
            max_count += -1
    return end_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([]))
    #print(frequency_sort([4, 2, 6, 2, 6, 4, 4, 4, 8, 8, 8, 8, 8]))
    #print(frequency_sort(['alex','bob', 'bob', 'carl', 'alex', 'bob','alex']))
