FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    num = str()
    if number > 99:
        num += FIRST_TEN[number//100-1] + ' ' + HUNDRED + ' '
    if number % 100 > 19:
        num += OTHER_TENS[number % 100 // 10 - 2] + ' '
        if number % 100 % 10 != 0:
            num += FIRST_TEN[number % 100 % 10 - 1]
    else:
        if number % 100 > 9:
            num += SECOND_TEN[number % 100 % 10] + ' '
        if 0 < number % 100 <= 9:
            num += FIRST_TEN[number % 100 % 10 - 1]
    return num.strip()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
