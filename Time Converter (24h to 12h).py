def time_converter(time):
    hh = int(time[:2])
    mm = int(time[3:])
    day = 'a.m.'
    if hh >= 12:
        day = 'p.m.'
    if hh == 0 and mm == 0:
        return '12:00' + '{}'.format(day)
    if hh % 12 >= 0 and (mm != 0):
        if hh > 12:
            hh = hh - 12
    if mm < 10:
        mm = '0' + str(mm)
    return '{0}:{1} '.format(hh, mm) + '{}'.format(day)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('00.00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert time_converter('12:30') == '12:30 p.m.'
    #assert time_converter('09:00') == '9:00 a.m.'
    #assert time_converter('23:15') == '11:15 p.m.'
    #print("Coding complete? Click 'Check' to earn cool rewards!")
