import itertools


def chance(dice, size, target):
    prev_proc = 1 / size
    if dice == 1:
        return {x: prev_proc for x in range(1, size+1)}
    elif dice == 2:
        nums = {}
        proc = {}
        for i in itertools.product(list(range(1, size+1)), list(range(1, size+1))):
            nums.setdefault(sum(i), 0)
            nums[sum(i)] += 1
        for k in nums.keys():
            proc.setdefault(k, 0)
            proc[k] = 1/size**2*nums[k]
        return proc
    else:
        proc1 = chance(dice-1, size, target)
        proc = {}
        for i in proc1.keys():
            for k in list(range(1, size+1)):
                proc.setdefault(i+k, 0)
                proc[i+k] += proc1[i]*prev_proc

        return proc

def probability(dice_number, sides, target):
    if dice_number*1 > target or dice_number * sides < target:
        return 0.0000
    else:
        # print(chance(dice_number, sides, target)[target])
        return chance(dice_number, sides, target)[target]

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
