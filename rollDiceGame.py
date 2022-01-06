# coding=utf-8

import random
import pylab


def roll_dice(numRoll):
    one = 0.0
    prob = 1 / 6
    for i in range(numRoll):
        if random.random() < prob:
            one += 1.0
    """Use func of random.choice()"""
    # for i in range(numRoll):
    #     if random.choice([1,2,3,4,5,6]) == 6:
    #         six += 1.0
    return one/numRoll

def roll_dice_simulation(num_rolls_per_trial, num_trial):
    frac_six = []
    for i in range(num_trial):
        frac_six.append(roll_dice(num_rolls_per_trial))
    return frac_six

def stdDev(X: list) -> float:
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) **2
    return  (tot/len(X)) ** 0.5


def label_plot(num_roll, num_trial, mean, sd):
    pylab.title(str(num_trial) + ' trials of ' + str(num_roll) + ' rolls each')
    pylab.xlabel('Fraction of Six Rolled')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin) * 0.02 , (ymax - ymin) /2,
               'Mean = ' + str(round(mean,5)) + '\nSD = ' + str(round(sd,5)))


def make_plot(nf1,nt):
    fracSix1 = roll_dice_simulation(nf1,nt)
    mean1 = sum(fracSix1) / float(len(fracSix1))
    sd1 = stdDev(fracSix1)
    pylab.hist(fracSix1, bins = 30)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    label_plot(nf1,nt,mean1,sd1)
    # pylab.figure()


def rollDice(num_of_dice,target):
    numerator = 0.0
    for i in range(num_of_dice):
        if random.choice([1,2,3,4,5,6]) == target:
            numerator += 1
    return numerator / num_of_dice


def rollDice_sim(num_of_dice,target: int, num_trial: int = 1000):
    frac_target = []
    for i in range(num_trial):
        frac_target.append(rollDice(num_of_dice,target))
    return frac_target

def label_plot1(num_of_dice, num_trial, mean, sd):
    pylab.title(str(num_trial) + ' trials of ' + str(num_of_dice) + ' dices rolls once each')
    pylab.xlabel('Fraction of Rolled 5 in 12 Dices')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin) * 0.02 , (ymax - ymin) /2,
               'Mean = ' + str(round(mean,5)) + '\nSD = ' + str(round(sd,5)))


def make_plot(nf1,nt):
    fracSix1 = roll_dice_simulation(nf1,nt)
    mean1 = sum(fracSix1) / float(len(fracSix1))
    sd1 = stdDev(fracSix1)
    pylab.hist(fracSix1, bins = 30)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    label_plot(nf1,nt,mean1,sd1)
    # pylab.figure()



# class dice_game():
#     def __init__(self, one, two, three, four, five, six):
#         self.one = 0.0
#         self.two = 0.0
#         self.three = 0.0
#         self.four = 0.0
#         self.five = 0.0
#         self.six = 0.0


def main():
    # make_plot(1000, 10000)
    # pylab.show()
    print(rollDice_sim(12,5))



if __name__ == '__main__':
    main()
