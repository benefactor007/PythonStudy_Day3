# coding = utf-8

import random

import pylab

from func_Collection import sort
from func_Collection import stdDev


class diceGame(object):
    cur_table = []

    def __init__(self, testerName, rolls, hand_dices=None):
        self.testerName = testerName
        self.rolls = rolls
        if hand_dices == None:
            hand_dices = []
        self.hand_dices = hand_dices

    def roll_dice(self):
        self.hand_dices = []
        for i in range(self.rolls):
            self.hand_dices.append(random.choice([1, 2, 3, 4, 5, 6]))
        return self.hand_dices

    def add_dices_to_talbe(self):
        diceGame.cur_table += self.hand_dices

    # def get_cur_talbe(self):
    #     print("the current table is " + str(diceGame.cur_table))
    #     return diceGame.cur_table

    def reset_dices(self):
        for element in self.hand_dices:
            diceGame.cur_table.remove(element)
        print(self.testerName + " reset his dices")
        diceGame.cur_table += self.roll_dice()

    def __str__(self):
        return "Tester Name: " + str(self.testerName) + "\n" + \
               "Rolls: " + str(self.rolls) + "\n" + \
               "Owned dices" + str(self.hand_dices)
        # "trails: " + str(self.trials)


class diceTrial(diceGame):
    def __init__(self, testerName, rolls, trials, trialsList=None, newL=None):
        super().__init__(testerName, rolls)
        self.trials = trials
        if trialsList is None:
            trialsList = []
        self.trialsList = trialsList
        if newL is None:
            newL = []
        self.newL = newL

    def roll_dice_trials(self):
        # L = []
        for i in range(self.trials):
            self.trialsList.append(sort(self.roll_dice()))
        return self.trialsList

    def get_result_each_trial(self):
        L = [0, 0, 0, 0, 0, 0]
        for i in self.trialsList:
            for j in i:
                for k in range(len(L)):
                    if j == k + 1:
                        L[k] += 1
            self.newL.append(L)
            L = [0, 0, 0, 0, 0, 0]
        return self.newL

    def get_target_each_roll(self, target):
        score_each_roll = []
        for i in self.newL:
            score_each_roll.append(i[target - 1])
        return sort(score_each_roll)

    def __str__(self):
        prefix = super().__str__()
        return prefix + "\n" + "trails: " + str(self.trials)


class dice_plot(diceTrial):
    """ Nice try but useless"""
    minExp = 2
    maxExp = 20
    yAxis = []

    # dice_plot_list = []

    def yAxis_exp(self):
        for exp in range(self.minExp, self.maxExp):
            self.yAxis.append(2 ** exp)
        return self.yAxis

    def roll_dice_by_exp(self):
        for i in self.yAxis:
            self.trialsList.append(sort(super().roll_dice()))
        return self.trialsList

    def plot(self):
        self.yAxis_exp()
        self.roll_dice_by_exp()
        self.get_result_each_trial()
        # pylab.plot(self.get_target_each_roll(6), self.yAxis , 'bo')
        pylab.hist(self.get_target_each_roll(6))
        pylab.show()  #


def main():
    t1 = diceGame("Jon", 10)
    print(t1)
    print(t1.roll_dice())
    t2 = diceGame("Dynasty", 2)
    print(t2)
    print(t2.roll_dice())
    temp_trial = 50000
    t3 = diceTrial("LOL", 20, temp_trial)
    print(t3)
    # print(t3.roll_dice_trials())
    # print(t3.trialsList)
    # print(t3.get_result_each_trial())
    t3.roll_dice_trials()
    t3.get_result_each_trial()
    pointNum = 6
    # print(t3.get_target_each_roll(pointNum))
    # pylab.plot(t3.get_target_each_roll(pointNum), "r" ,label="get " + str(pointNum) +" in 1000 trials")
    t3.get_target_each_roll(pointNum)
    # print(t3.xAis_exp())
    print("The std of " + str(pointNum) + " is " + str(stdDev(t3.get_target_each_roll(pointNum))))
    print("The mean of " + str(pointNum) + " is " + str(
        sum(t3.get_target_each_roll(pointNum)) / float(len(t3.get_target_each_roll(pointNum)))))
    pylab.title("get " + str(pointNum) + " in " + str(temp_trial) + " trials")
    pylab.hist(t3.get_target_each_roll(pointNum), bins=20)
    pylab.figure()
    # pointNum = 5
    # print("The std of " + str(pointNum) + " is " + str(stdDev(t3.get_target_each_roll(pointNum))))
    # pylab.title("get " + str(pointNum) + " in " + str(temp_trial) + " trials")
    # pylab.hist(t3.get_target_each_roll(pointNum), bins=20)
    # pylab.figure()
    # pointNum = 4
    # print("The std of " + str(pointNum) + " is " + str(stdDev(t3.get_target_each_roll(pointNum))))
    # pylab.title("get " + str(pointNum) + " in " + str(temp_trial) + " trials")
    # pylab.hist(t3.get_target_each_roll(pointNum), bins=20)
    # pylab.figure()
    # pointNum = 3
    # print("The std of " + str(pointNum) + " is " + str(stdDev(t3.get_target_each_roll(pointNum))))
    # pylab.title("get " + str(pointNum) + " in " + str(temp_trial) + " trials")
    # pylab.hist(t3.get_target_each_roll(pointNum), bins=20)
    # pylab.figure()
    # pointNum = 2
    # print("The std of " + str(pointNum) + " is " + str(stdDev(t3.get_target_each_roll(pointNum))))
    # pylab.title("get " + str(pointNum) + " in " + str(temp_trial) + " trials")
    # pylab.hist(t3.get_target_each_roll(pointNum), bins=20)
    # pylab.figure()
    # pointNum = 1
    # print("The std of " + str(pointNum) + " is " + str(stdDev(t3.get_target_each_roll(pointNum))))
    # pylab.title("get " + str(pointNum) + " in " + str(temp_trial) + " trials")
    # pylab.hist(t3.get_target_each_roll(pointNum), bins=20)
    # pylab.figure()
    pylab.show()

    # pylab.title("get " + str(pointNum) +" in 50000 trials")
    # pylab.show()


def main2():
    t4 = dice_plot("Xuping", 24, 1000)
    t4.plot()
    print(t4.get_target_each_roll(6))


def main3():
    """set a roll dices game"""
    play1 = diceGame("Jon", 8)
    play2 = diceGame("Dynasty", 8)
    play3 = diceGame("Frank", 8)
    print(play1)
    print(play2)
    print(play3)
    print(play1.roll_dice())
    print(play1.roll_dice())
    play1.add_dices_to_talbe()
    print("The current table is" + str(diceGame.cur_table))
    play2.roll_dice()
    play2.add_dices_to_talbe()
    print("The current table is" + str(diceGame.cur_table))
    print(play1)
    print(play2)
    play1.reset_dices()
    print(play1)
    print("The current table is" + str(diceGame.cur_table))
    play3.roll_dice()
    play3.add_dices_to_talbe()
    print("The current table is" + str(diceGame.cur_table))
    # player1 = diceTrial("Jon", 8, 100)
    # player1.roll_dice_trials()
    # player1.get_result_each_trial()
    # pointNum = 6
    # player1.get_target_each_roll(pointNum)
    # print(player1.get_target_each_roll(pointNum))


if __name__ == '__main__':
    main()
    # main2()
    # main3()
