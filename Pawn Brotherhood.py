def safe_pawns(pawns: set) -> int:
    incoming_data_list = list(pawns)
    literal_dickt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    safe_zone_set = set()

    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    for _ in incoming_data_list:
        x = int(_[1]) + 1

        if literal_dickt[_[0]] == 1:
            y1 = literal_dickt[_[0]] + 1
            if x <= 8:
                safe_zone_set.add((str(get_key(literal_dickt, y1))+str(x)))
        elif literal_dickt[_[0]] == 8:
            y2 = literal_dickt[_[0]] - 1
            if x <= 8:
                safe_zone_set.add((str(get_key(literal_dickt, y2))+str(x)))
        else:
            y1 = literal_dickt[_[0]] + 1
            y2 = literal_dickt[_[0]] - 1
            if x <= 8:
                safe_zone_set.add((str(get_key(literal_dickt, y1))+str(x)))
                safe_zone_set.add((str(get_key(literal_dickt, y2))+str(x)))

    safe_pawn = 0
    for end in incoming_data_list:
        if end in safe_zone_set:
            safe_pawn += 1
    return safe_pawn

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) #== 6
    safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) #== 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
