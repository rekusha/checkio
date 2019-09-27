def checkio(text: str) -> str:
    work_dickt = {}
    work_list = []
    max_enter = 0
    text=text.lower()
    for _ in text:
        if _.isalpha():
            if _ in work_dickt:
                work_dickt[_] += 1
            else:
                work_dickt[_] = 1

    for i in work_dickt:
        if work_dickt[i] > max_enter:
            max_enter = work_dickt[i]

    for i in work_dickt:
        if work_dickt[i] == max_enter:
            work_list.append([i, work_dickt[i]])
    work_list.sort()
    return work_list[0][0]

if __name__ == '__main__':
    print(checkio("Hello World!"))
