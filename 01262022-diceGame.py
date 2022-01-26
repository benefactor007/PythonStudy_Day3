# coding=utf-8


class Dice(object):
    def __init__(self):
        import random
        self.dice = random.choice([1, 2, 3, 4, 5, 6])

    def __str__(self):
        return str(self.dice)


class Dices(object):
    def __init__(self, dice_num = 1):
        self.dices = []
        self.dices_num = dice_num
        for dice in range(dice_num):
            self.dices.append(Dice())


    def __str__(self):
        s = ""
        for i in range(len(self.dices)):
            s = s + " " * i + str(self.dices[i]) + "\n"
        return s

    def re_roll(self):
        self.dices = []
        for dice in range(self.dices_num):
            self.dices.append(Dice())
        return self.dices



# class Player():
#     def __init__(self, name=""):
#


def main():
    # t1 = Dice()
    # print(t1)
    # t2 = Dice()
    # print(t2)
    t1 = Dices(8)
    print(t1)
    # print(t1.dices)
    t1.re_roll()
    print(t1)


if __name__ == '__main__':
    main()
