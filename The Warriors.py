class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(fight(chuck, bruce))# == True
    print(fight(dave, carl))# == False
    print(chuck.is_alive)# == True
    print(bruce.is_alive)# == False
    print(carl.is_alive)# == True
    print(dave.is_alive)# == False
    print(fight(carl, mark))# == False
    print(carl.is_alive)# == False
    print("Coding complete? Let's try tests!")
